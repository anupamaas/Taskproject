from django.db.models.fields import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Drop,Dropdown,Down,Dependent
from .forms import DropForm
from django.views.generic import CreateView, UpdateView, ListView


# Create your views here.
# class DropListView(ListView):
#     model=Dependent
#     context_object_name = 'dependent'
#
# class DropCreateView(CreateView):
#     model=Dependent
#     form_class=DropForm
#     success_url = reverse_lazy('dependent_changelist')
#
# class DropUpdateView(UpdateView):
#     model = Dependent
#     form_class = DropForm
#     success_url = reverse_lazy('dependent_changelist')
# def load_branches(request):
#     district_id=request.GET.get('country')
#     branches=Drop.objects.filter(district_id=district_id).order_by('name')
#     return render(request,'templates/branch_dropdown_list_options.html',{'branches':branches})

def index(request):
    return render(request,'index.html')
def login (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"new.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']


        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
            print("user created")
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")




def final(request):
    messages.info(request, "Application Accepted")
    return render(request,"final.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    if request.method=="POST":
        name=request.POST.get("name",)
        birthdate = request.POST.get("birthdate", )
        age = request.POST.get("age",)
        gender = request.POST.get("gender", )
        number = request.POST.get("number", )
        mail  = request.POST.get("mail ",)
        address = request.POST.get("address",)
        district = request.POST.get("district",)
        branch = request.POST.get("branch",)
        account = request.POST.get("account",)
        credit = request.POST.get("credit",)
        debit = request.POST.get("debit",)
        cheque = request.POST.get("cheque",)
        dependent=Dependent(name=name,birthdate=birthdate,age=age,gender=gender,number=number,mail=mail,address=address,district=district,branch=branch,account=account,credit=credit,debit=debit,cheque=cheque)


    return render(request, 'form.html')

# def add(request,id):
#     dependent=Dependent.objects.get(id=id)
#     form= DropForm (request.POST or None,instance=dependent)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'add.html',{'form':form,'dependent':dependent})


def new(request):
    return render(request,'new.html')



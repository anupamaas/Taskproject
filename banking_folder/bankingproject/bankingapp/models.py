from django.db import models


# Create your models here.
class Drop(models.Model):
    name=models.CharField(max_length=250)
    def __str__ (self):
         return'{}'.format(self.name)

class Dropdown(models.Model):
    district=models.ForeignKey(Drop,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

    def __str__ (self):
        return'{}'.format(self.name)
class Down(models.Model):

    name = models.CharField(max_length=250)

    def __str__ (self):
        return'{}'.format(self.name)

class Dependent(models.Model):
    name = models.CharField(max_length=250)
    birthdate = models.DateField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=250)
    number = models.IntegerField(null=True)
    mail = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    district = models.ForeignKey(Drop, on_delete=models.SET_NULL,null=True)
    branch =models.ForeignKey(Dropdown,on_delete=models.SET_NULL,null=True)
    account = models.ForeignKey(Down, on_delete=models.SET_NULL,null=True)
    credit=models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    cheque = models.BooleanField(default=False)


    def __str__(self):
        return '{}'.format(self.name)



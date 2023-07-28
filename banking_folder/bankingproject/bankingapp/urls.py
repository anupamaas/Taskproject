from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
      path('form',views.form,name='form'),
    path('final',views.final,name='final'),
path('new',views.new,name='new'),
path('logout',views.logout,name='logout'),
# path('add',views.add,name='add'),
#     path('create/',views.DropCreateView.as_view(),name='drop_create'),
#     path('<int:pk>/',views.DropUpdateView.as_view(),name='drop_change'),
#     path('list/', views.DropCreateView.as_view(), name='drop_changelist'),

]
from django.urls import path

from .import views  
urlpatterns=[
    
    # entire details are view only by AdminPanel
    path('AdminPanel/',views.admin,name='AdminPanel'),
    # this one is for compamy registeration
    path('register/',views.companyRegister,name='register'),
    # below one for register_companie view
    path('dataview/',views.reaData,name='dataview'),
    # below one for user registration
    path('userRegister/',views.userRegister,name='userRegister'),
    # userRegistered datas are catched by below line code
    path('userData/',views.userData,name='usersData'),
    # page redirection for accept and reject
    path('approve/<int:regid>',views.accept,name='accept'),
    path('reject/<int:regid>',views.reject,name='reject'),
    # below code for login (users or companies)
    path('Login/<str:usertype>/',views.logins,name='Login'),
    
    # path('sucess/',views.sucess,name='sucess'),
    
]
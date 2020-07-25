"""HospitalManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sitehandler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('about/',aboutpage,name='aboutpage'),
    path('login/',loginpage,name='loginpage'),
    path('createaccount',createaccountpage,name='createaccountpage'),
    path('admin_login/',Login_admin,name='login_admin'),
    path('adminhome/',AdminHome,name='adminhome'),
    path('adminlogout/',Logout_admin,name='adminlogout'),
    path('adminaddDoctor/',adminaddDoctor,name='adminaddDoctor'),
    path('adminviewDoctor/',adminviewDoctor,name='adminviewDoctor'),
    path('adminDeleteDoctor<int:pid><str:email>',admin_delete_doctor,name='admin_delete_doctor'),
    path('adminaddReceptionist/',adminaddReceptionist,name='adminaddReceptionist'),
    path('adminviewReceptionist/',adminviewReceptionist,name='adminviewReceptionist'),
    path('adminDeleteReceptionist<int:pid>,<str:email>',admin_delete_receptionist,name='admin_delete_receptionist'),
    path('adminviewAppointment/',adminviewAppointment,name='adminviewAppointment'),
    path('home/',Home,name='home'),
    path('profile/',profile,name='profile'),
    path('makeappointments/',MakeAppointments,name='makeappointments'),
    path('viewappointments/',viewappointments,name='viewappointments'),
    path('PatientDeleteAppointment<int:pid>',patient_delete_appointment,name='patient_delete_appointment'),
    path('logout/',Logout,name='logout'),
]


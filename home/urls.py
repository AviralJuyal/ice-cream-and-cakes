from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" ,views.index , name = 'home' ),

    path("about" ,views.about , name = 'about' ),
 
    path("icecream" ,views.icecream , name = 'icecream' ),

    path("buy" , views.buy , name = 'buy' ),

    path ("cake" , views.cake , name = 'cake'),
 
    path("contact" ,views.contact , name = 'contact' ),

    path("login" , views.loginuser , name = 'login'),
     
    path ("logout" ,views.logoutuser , name = 'logout')

    
]

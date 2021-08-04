from django.shortcuts import render ,HttpResponse 
from datetime import datetime
from home.models import Cakes ,  Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def index(request):
  
    return render(request , 'index.html' )

def buy(request):
  
    return render(request , 'buy.html' )

def about(request):
    return render(request , 'about.html' )

    # return HttpResponse("This tells u about the page info")

def icecream(request):
    return render(request , 'icecream.html' )

def cake(request):

    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        desc = request.POST.get('desc')  
        print(name , number )
        cake = Cakes(name=name , number= number, desc=desc ,date= datetime.today() )
        cake.save()
        messages.success(request , 'Your order is placed we will contact u soon!')
    return render(request, 'cake.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name= name , email= email , desc= desc , date= datetime.today() )
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request , 'contact.html' )

def loginuser(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)

            if user is not None:
            # A backend authenticated the credentials
                login(request , user)
                return render (request , 'imp.html')
        
            else:
                
            # No backend authenticated the credentials
                return render (request , 'login.html')


    return render (request , 'login.html')

def logoutuser(request):
    logout(request)
    return render (request , 'login.html')
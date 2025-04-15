from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact   
from .forms import ContactForm
from .models import Contact as ContactModel 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


  
# Create your views here.
def index(request):
    return render(request, "index.html")

def loginuser(request):
 
    if request.method =="POST":
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(username=username, password=password)
     
        if user is not None:
         print(username,password)
         login(request,user)
         return redirect("/index/")
         
        else:
         return render(request, "login.html")
    
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    
    return redirect("/")



def about(request):
    return render(request, "about.html")
 

# def contact(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
        
    #     new_contact = Contact(name=name,email=email,subject=subject)
    #     new_contact.save()
    #     return render(request, "contact.html", {'success': True})
    # return render(request, "contact.html")

def locations(request):
    return render(request, "locations.html")
def register(request):
    return render(request, "register.html")
 
 
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact1.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    
    return render(request, 'contact1.html', {'form': form})

 

 
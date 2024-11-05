
from .models import UserProfile
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.hashers import check_password

# Create your views here.
from django.http import HttpResponse
from .models import menu

def homepage(request):
    menu_items = menu.objects.all()  # Retrieve all menu items
    return render(request, 'index.html', {'menu': menu_items})

def chinese(request):
        return render(request,'chinese.html')
def desi(request):
        return render(request,'desi.html')
def fastfood(request):
        return render(request,'fastfood.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserProfile.objects.get(email=email)
            if user.password == password:  
                return redirect("/")  
            else:
                messages.error(request, "Incorrect password. Please try again.")
        except UserProfile.DoesNotExist:
            messages.error(request, "Email does not exist.")

        return redirect("login")  

    return render(request, "login.html")
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            UserProfile.objects.create(username=username, email=email, password=password)
            return redirect('login')
        except IntegrityError:
            return render(request, "signup.html", {"error": "Username or email already exists."})
        
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, "signup.html")


    return render(request, "signup.html")
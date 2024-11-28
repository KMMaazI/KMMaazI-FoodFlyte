from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User 
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Menu_items,Restaurant,Orders
from django.contrib.auth.decorators import login_required


@login_required
def place_order(request, menu_item_id):
    menu_item = get_object_or_404(Menu_items, id=menu_item_id)

    if request.method == "POST":
        address = request.POST.get("address")
        quantity = int(request.POST.get("quantity", 1))  # Default quantity to 1 if not provided
        price = menu_item.price * quantity  # Calculate the total price

        # Create the order in the database
        Orders.objects.create(
            user=request.user,
            menu_item=menu_item,
            address=address,
            quantity=quantity,
            price=price
        )

        return redirect("homepage")  # Redirect to the homepage after placing the order

    return render(request, "place_order.html", {"menu_item": menu_item})

@login_required
def orders_list(request):
    # Fetch all orders placed by the logged-in user
    orders = Orders.objects.filter(user=request.user).order_by('-created_at')  # Orders sorted by creation date (latest first)
    return render(request, 'orders_list.html', {'orders': orders})

def search_restaurant(request):
    query = request.GET.get('q', '')
    
    # If there's no query, fetch all restaurants
    if query:
        restaurants = Restaurant.objects.filter(name__icontains=query)
    else:
        # Fetch all restaurants if no query is provided
        restaurants = Restaurant.objects.all()

    return render(request, 'index.html', {'restaurants': restaurants, 'query': query})
def restaurant_menu(request, restaurant_name):
    # Get the restaurant object by name
    restaurant = get_object_or_404(Restaurant, name=restaurant_name)
    # Get the associated menu items
    menu_items = restaurant.menu_items.all()
    
    return render(request, 'restaurant.html', {
        'restaurant': restaurant,
        'menu_items': menu_items
    })

def homepage(request):
    Restaurant_items = Restaurant.objects.all()  # Retrieve all menu items
    return render(request, 'index.html', {'Restaurant': Restaurant_items})

def chinese(request):
        return render(request,'chinese.html')
def desi(request):
        return render(request,'desi.html')
def fastfood(request):
        return render(request,'fastfood.html')

# def login(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         try:
#             user = UserProfile.objects.get(email=email)
#             if user.password == password:  
#                 return redirect("/")  
#             else:
#                 messages.error(request, "Incorrect password. Please try again.")
#         except UserProfile.DoesNotExist:
#             messages.error(request, "Email does not exist.")

#         return redirect("login")  

#     return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)  # Hash the password
            user.save()
            return redirect('login_view')
        except IntegrityError:
            return render(request, "signup.html", {"error": "Username or email already exists."})

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in and start a session
            return redirect("/")  # Redirect to the homepage
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login_view")

    return render(request, "login.html")


def logout_view(request):
    logout(request)  # Log out the user
    return redirect("homepage")
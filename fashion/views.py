from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserProfile, UpdatePassword, UpdateInfo
from payments.forms import ShippingForm
from payments.models import ShippingAddress
from django import forms
import json
from cart.cart import Cart


# Create your views here.
def home(request):
    return render(request, "fashion/home.html", {
        "products": Product.objects.all()
    })

def about(request):
    return render(request, "fashion/about.html", {})

def contact(request):
    return render(request, "fashion/contact.html", {})

def login_user(request):
    if request.method == "POST":
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)

           current_user = Profile.objects.get(user__id=request.user.id)
           saved_cart = current_user.old_cart

           if saved_cart:
                convert_cart = json.loads(saved_cart)
                cart = Cart(request)
                
                for key, value in convert_cart.items():
                    cart.db_add(product=key, quantity=value)

           messages.success(request, ("You Have Been Logged In!"))
           return redirect("home")
       else:
           messages.success(request, ("There Was An Error. Please Try Again!"))
           return redirect("login")
    else:
       return render(request, "fashion/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out!"))
    return redirect("home")

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You Have Successfully Registered!"))
            return redirect("home")
        else:
            messages.error(request, form.errors)
            return redirect("register")
    else:
        form = SignUpForm(request.POST)
        return render(request, "fashion/register.html", {
            "form":form
        })
    
def product(request,pk):
    return render(request, "fashion/product.html", {
        "product": Product.objects.get(id=pk)
    })  

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, "fashion/category.html", {
            "products":  products,
            "category": category
        }) 
    except:
          messages.success(request, ("Ooops! The Category Is Not Available"))
          return redirect("home") 
     
    
#Update User Profile
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserProfile(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, ('You Have Updated Your Profile'))
            return redirect("home")
        else:
            return render(request, "fashion/update_user.html", {
                "user_form":user_form
            })
    else:
        messages.success(request, ('You are Already Logged in!!'))
        return redirect("home")
     
#Update password
def update_pw(request):
    if request.user.is_authenticated:
        current_user = request.user 
        if request.method == 'POST':
            pw_form = UpdatePassword(current_user, request.POST)
            if pw_form.is_valid():
                pw_form.save()
                messages.success(request, ('You Have Successfully Updated Your Password!! Please Login Again!'))
                return redirect("login")
            else:
                for error in list(pw_form.errors.values()):
                    messages.error(request, error)
                    return redirect("update_pw")
        else:
            pw_form = UpdatePassword(current_user)
            return render(request, "fashion/update_pw.html", {
                'pw_form':pw_form
        })

    else:
        messages.success(request, ('You Must Be Logged In To View That Page!'))

    
def update_info(request):
    if request.user.is_authenticated:
        try:
            current_user = Profile.objects.get(user__id=request.user.id)
            info_form = UpdateInfo(request.POST or None, instance=current_user)

            shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
            shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
            if info_form.is_valid() or shipping_form.is_valid():
                info_form.save()
                shipping_form.save()
                
                messages.success(request, ('You Have Successfully Updated Your Info!'))
                return redirect("home")
            else:
                return render(request, "fashion/update_info.html", {
                "info_form":info_form,
                "shipping_form":shipping_form
                })

           
            
        except Profile.DoesNotExist:
            return redirect('update_user')

        
    else:
        messages.success(request, ('You Must Be Logged In To Access The Page!!'))
        return redirect("home")


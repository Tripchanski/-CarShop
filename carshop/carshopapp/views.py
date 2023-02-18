from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Car, Description

# Create your views here.


def show_reg(request):
    context = {}
    if request.method == "POST": 
            login = request.POST.get("login")
            password = request.POST.get("password")
            password_confirm = request.POST.get("password_confirm")
            context["login"] = login
            context["password"] = password
            context["password_confirm"] = password_confirm
            if password == password_confirm:
                try:
                    User.objects.create_user(username = login, password = password)
                    return redirect('login')
                except IntegrityError:
                    context['error'] = 'Користувач вже існує' 
            else:
                context["error"] = "Паролі не спiвпадають"

    return render(request, 'reg.html', context)



def show_login(request):
    context = {}
    if request.method == 'POST':
        login_user = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username = login_user, password = password)
        if user != None:
            login(request, user)
            return redirect('carshop')
        else:
            context['error'] = 'Логін або пароль невірні'
            
    return render(request, 'login.html', context)



def show_carshop(request):
    product = Car.objects.get(pk=1)
    if request.user.is_authenticated:
        if request.method == 'POST':
            description = request.POST.get("description")
            author = request.user.username
            print(description)
            Description.objects.create(description = description, author = author)
            
        descriptions = Description.objects.all()
        return render(request, "carshop.html", context= {'product': product, 'descriptions': descriptions})
    else:
        return redirect('login')
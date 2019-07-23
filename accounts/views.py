from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterForm, LoginForm
from gestpermis.models import CapitalPoint
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            #if data['password'] == data['password_confirm']:
                #print(data)
            new_user = User.objects.create(
                first_name = data['nom'],
                last_name = data['prenom'],
                username = data['username'],
                email = data['email'],
            )

            new_user.set_password(data['password'])
            new_user.save()
            return redirect('article:home')
    context = {
        'form':form
    }

    return render(request, 'accounts/register.html', context)
   

#Connexion func

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('article:home')

            
    context = {
            'form':form
        }

    return render(request, 'accounts/login.html', context)
# Create your views here.

def logout_view(request):
    logout(request)
    return None
    # return render(request, 'accounts/login.html', context)
    # return redirect('article:home')
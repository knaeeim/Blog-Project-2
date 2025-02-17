from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('register')
    else:
        form = RegistrationFrom()
    return render(request, "register.html", {'form' : form, 'type' : 'Registration'})


# def user_login(request):
#     if request.user.is_authenticated:
#         return redirect('profile')
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         print('from 28')
#         if form.is_valid():
#             print('from 29')
#             user_name = form.cleaned_data['username']
#             user_password = form.cleaned_data['password']
#             user = authenticate(username = user_name, password = user_password)
#             print('from 32')
#             if user is not None:
#                 print('from 34')
#                 messages.success(request, "Logged in successfully")
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 print('from else')
#                 messages.warning(request, "Login Credentials are incorrect")
#                 # return redirect('register')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                messages.success(request, "Logged in successfully")
                login(request, user)
                return redirect('profile')
        else:
            messages.warning(request, "Login credentials are incorrect")
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})
    

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out Successfully")
    return redirect('login')

@login_required
def change_user_data(request):
    # if request.user.is_authenticated:
        if request.method == "POST":
            change_data = changeUserData(request.POST, instance = request.user)
            if change_data.is_valid():
                change_data.save()
                messages.success(request, "Profile updated successfully")
                return redirect('profile')
        else:
            change_data = changeUserData(instance = request.user)
        return render(request, 'change.html', {'form' : change_data})
    # else:
    #     return redirect('login')

def update_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            change_password = PasswordChangeForm(request.user, data=request.POST)
            if change_password.is_valid():
                print(change_password.cleaned_data)
                change_password.save()
                messages.success(request, "Password updated successfully")
                update_session_auth_hash(request, change_password.user)
                return redirect('profile')
        else:
            change_password = PasswordChangeForm(request.user)
        return render(request, 'password.html', {'form' : change_password})
    else:
        return redirect('login') 
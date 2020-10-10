from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def customer_signup(request):
    form = SignupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        user_obj.password = make_password(user_obj.password)
        user_obj.user_type = 3
        user_obj.save()
        return redirect('usermodule:signin')
    return render(request, 'usermodule/signup.html', {'form': form})


def account_signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    form = SigninForm(request.POST or None)
    if form.is_valid():
        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password')
        user = authenticate(request, mobile=mobile, password=password)
        if user is not None:
            messages.success(request, "Logged In successfully!")
            login(request, user)
            if user.user_type in (1, 2):
                return redirect('seller_home')
            if user.user_type == 3:
                return redirect('homepage')
        else:
            messages.error(request, "Invalid Mobile number or Password!!!")
    return render(request, 'usermodule/signin.html', {'form': form})


@login_required
def customer_signout(request):
    logout(request)
    return redirect('homepage')


@login_required
def customer_profile(request):
    instance = User.objects.get(id=request.user.id)
    form = MyaccountForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, "Account updated successfully!")
        return redirect('usermodule:myaccount')
    return render(request, 'usermodule/myaccount.html', {'form': form})

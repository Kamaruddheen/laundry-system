from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .decorators import *
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


# Common signin for all account
def account_signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    form = SigninForm(request.POST or None)
    if form.is_valid():
        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password')
        user = authenticate(request, mobile=mobile, password=password)
        next_link = request.GET.get('next', None)
        print(next_link)
        if user is not None:
            login(request, user)
            if user.user_type in (1, 2):
                if next_link:
                    return redirect(next_link)
                else:
                    messages.success(request, "Signed In as Staff")
                    return redirect('staffmodule:staff_homepage')
            if user.user_type == 3:
                if next_link:
                    return redirect(next_link)
                else:
                    messages.success(request, "Signed In as Customer")
                    return redirect('homepage')
        else:
            messages.error(request, "Invalid Mobile number or Password!!!")
    return render(request, 'usermodule/signin.html', {'form': form})


@login_required
def account_signout(request):
    logout(request)
    messages.error(request, "Signed out successfully!!!")
    return redirect('homepage')


@user_is_owner
def staff_signup(request):
    form = SignupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        user_obj.password = make_password(user_obj.password)
        user_obj.user_type = 2
        user_obj.save()
        return redirect('staffmodule:staff_homepage')
    return render(request, 'staffmodule/staff_signup.html', {'form': form})


# Common account detail
@login_required
def account_profile(request):
    instance = User.objects.get(id=request.user.id)
    form = MyaccountForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, "Account updated successfully!")
        return redirect('usermodule:myaccount')
    return render(request, 'usermodule/myaccount.html', {'form': form})

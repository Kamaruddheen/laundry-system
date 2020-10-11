from django.shortcuts import redirect
from django.contrib import messages


def user_is_customer(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 3:
                return function(request, *args, **kwargs)
            else:
                messages.warning(request, 'Signin using Customer Account')
                return redirect(redirect('usermodule:signin').url+'?next='+request.path)
        else:
            return redirect(redirect('usermodule:signin').url+'?next='+request.path)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_staff(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 2 or request.user.user_type == 1:
                return function(request, *args, **kwargs)
            else:
                messages.warning(request, 'Signin using Staff Account')
                return redirect(redirect('usermodule:signin').url+'?next='+request.path)
        else:
            messages.info(request, 'Signin to continue')
            return redirect(redirect('usermodule:signin').url+'?next='+request.path)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_owner(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 1:
                return function(request, *args, **kwargs)
            else:
                messages.warning(request, 'Signin using Owner Account')
                return redirect(redirect('usermodule:signin').url+'?next='+request.path)
        else:
            messages.info(request, 'Signin to continue')
            return redirect(redirect('usermodule:signin').url+'?next='+request.path)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

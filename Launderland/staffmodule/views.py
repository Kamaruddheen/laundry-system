from django.contrib import messages
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect

from .forms import *
from .models import *
from usermodule.decorators import user_is_staff, user_is_owner


@user_is_staff
def staff_homepage(request):
    return render(request, 'staffmodule/index.html')


@user_is_staff
def service(request):
    services = Service.objects.all()
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        if request.user.user_type == 1:
            form.save()
        else:
            messages.warning(
                request, 'Staff cannot add a new Service. Only Owner can add new service')
    context = {'form': form, 'services': services}
    return render(request, 'staffmodule/service.html', context=context)


@user_is_owner
def service_edit(request, id):
    if request.method == "POST":
        service = request.POST.get('service')
        if Service.objects.filter(id=id).exists():
            demo = Service.objects.filter(service=service) or None
            if demo is None:
                Service.objects.filter(id=id).update(service=service)
                messages.info(request, 'Service edited successfully!!!')
            else:
                messages.info(request, 'No changes detected..')
        else:
            messages.info(request, 'Couldn\'t able to find the service')
        return redirect('staffmodule:service')
    else:
        return redirect('homepage')


@user_is_owner
def service_delete(request, id):
    service = get_object_or_404(Service, id=id)
    service.delete()
    messages.success(request, 'Deleted successfully!!!')
    return redirect('staffmodule:service')

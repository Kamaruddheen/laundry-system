from usermodule.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .forms import *
from .models import *
from usermodule.decorators import user_is_staff, user_is_owner
from django.utils.timezone import now, timedelta


# ? staff_homepage
@user_is_staff
def staff_homepage(request):
    return render(request, 'staffmodule/index.html')


# all user can view service
def service_view(request):
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


# all user can view Subservice
def sub_service_view(request, id):
    sub_service = Subservice.objects.filter(service=id)
    form = SubServiceForm(request.POST or None)
    if form.is_valid():
        if request.user.user_type == 1:
            form_obj = form.save(commit=False)
            form_obj.service = Service.objects.get(id=id)
            form_obj.save()
        else:
            messages.warning(
                request, 'Staff cannot add a new Service. Only Owner can add new service')
    context = {'form': form, 'sub_service': sub_service}
    return render(request, 'staffmodule/sub_service.html', context=context)


@user_is_owner
def sub_service_edit(request, id):
    if request.method == "POST":
        sub_service = request.POST.get('sub_service')
        price = request.POST.get('price')
        if Subservice.objects.filter(id=id).exists():
            demo = Subservice.objects.filter(
                sub_service=sub_service, id=id) or None
            prices = Subservice.objects.filter(price=price, id=id) or None
            if demo is None or prices is None:
                Subservice.objects.filter(id=id).update(
                    sub_service=sub_service)
                Subservice.objects.filter(id=id).update(price=price)
                messages.info(request, 'Subservice edited successfully!!!')
            else:
                messages.info(request, 'No changes detected..')
        else:
            messages.info(request, 'Couldn\'t able to find the Subservice')

        service = Subservice.objects.get(id=id)
        return redirect('staffmodule:subservices', id=service.service_id)
    else:
        return redirect('homepage')


@user_is_owner
def sub_service_delete(request, id):
    subservice = Subservice.objects.get(id=id)
    subservice.delete()
    messages.success(request, 'Deleted successfully!!!')
    return redirect('staffmodule:subservices', id=subservice.service_id)


@user_is_staff
def staff_list(request):
    staffs = User.objects.filter(user_type=2)
    return render(request, 'staffmodule/staff_list.html', {'staffs': staffs})


@user_is_staff
def staff_details(request, id):
    customer = get_object_or_404(User, id=id)
    status_time = (now() - timedelta(hours=24)
                   ) < (customer.last_login or (now() - timedelta(hours=24)))
    staff = get_object_or_404(User, id=id)
    context = {'staff': staff, 'status_time': status_time}
    return render(request, 'staffmodule/staff_detail.html', context)

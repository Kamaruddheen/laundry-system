from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from usermodule.decorators import *
from usermodule.forms import User

from .forms import *


def laundry(request):
    return render(request, 'laundry/laundry.html')


@user_is_customer
def sub_service(request):
    if request.method == "GET":
        service = request.GET.get('service')
        subservice = Subservice.objects.filter(
            service=service).order_by('sub_service')
        context = {'sub_service': subservice}
        return render(request, 'laundry/sub_service.html', context)


@user_is_customer
def Bookings(request):
    form = BookingForm(request.POST or None)
    staff_free = User.objects.filter(user_type=2, staff_status=False)
    if form.is_valid():
        if staff_free:
            quantity = request.POST.get('quantity')
            price_id = request.POST.get('sub_service')
            price = Subservice.objects.get(id=price_id)
            staff_name = str(staff_free[0].first_name)
            booking_obj = form.save(commit=False)
            booking_obj.amount = price.price * float(quantity)
            booking_obj.cust_id = User.objects.get(id=request.user.id or None)
            booking_obj.assigned_staff = User.objects.get(
                mobile=staff_free[0].mobile)
            booking_obj.save()
            User.objects.filter(mobile=staff_free[0].mobile).update(
                staff_status=True)
            messages.success(
                request, staff_name + " will take care of your laundry")
            return redirect('laundry:mybooking')
        else:
            messages.info(
                request, "Our Staffs are currently busy. Try after some time...")
        return redirect('laundry:laundry')
    return render(request, 'laundry/booking.html', {'form': form})


@user_is_customer
def Mybookings(request):
    bookings = Booking.objects.filter(
        cust_id=request.user.id).order_by('booked_on').reverse()
    return render(request, 'laundry/booking_list.html', {'bookings': bookings})


@user_is_customer
def Booking_details(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'laundry/booking_details.html', {'booking': booking})


@user_is_staff
def staff_all_booking(request):
    bookings = None
    if request.user.user_type == 1:
        bookings = Booking.objects.all().order_by('booked_on').reverse()
    elif request.user.user_type == 2:
        bookings = Booking.objects.filter(
            assigned_staff=request.user.id).order_by('booked_on').reverse()
    return render(request, 'laundry/staff_booking.html', {'booking': bookings})


@user_is_staff
def staff_booking_edit(request, id):
    booking = get_object_or_404(Booking, id=id)
    staff_id = booking.assigned_staff.id
    myform = UpdateBookingForm(
        request.POST or None, instance=booking, request=request)
    if myform.is_valid():
        form_obj = myform.save(commit=False)
        if form_obj.status == "delivered" or form_obj.status == "canceled":
            form_obj.save()
            User.objects.filter(id=staff_id).update(
                staff_status=False)
        else:
            form_obj.save()
            User.objects.filter(id=staff_id).update(
                staff_status=True)
        messages.success(
            request, "You have successfully changed Status to \"" + form_obj.status + "\"")
    context = {'form': myform, 'booking': booking, }
    return render(request, 'laundry/staff_edit_booking.html', context=context)

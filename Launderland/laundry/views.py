from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from usermodule.decorators import user_is_customer
from usermodule.forms import User
from .forms import *


def laundry(request):
    return render(request, 'laundry/laundry.html')


@user_is_customer
def Bookings(request):
    form = BookingForm(request.POST or None)
    staff_free = User.objects.filter(user_type=2, staff_status=False)
    if form.is_valid():
        if staff_free:
            staff_name = str(staff_free[0].first_name)
            booking_obj = form.save(commit=False)
            booking_obj.cust_id = User.objects.get(id=request.user.id)
            booking_obj.assigned_staff = User.objects.get(mobile=staff_free[0])
            booking_obj.save()
            User.objects.filter(mobile=staff_free[0]).update(
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

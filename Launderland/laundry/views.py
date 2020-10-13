from django.contrib import messages
from django.shortcuts import redirect, render
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
        if staff_free[0]:
            booking_obj = form.save(commit=False)
            booking_obj.cust_id = User.objects.get(id=request.user.id)
            booking_obj.assigned_staff = User.objects.get(mobile=staff_free[0])
            booking_obj.save()
            # staff_free[0].update(staff_status=True)
            messages.success(
                request, str(staff_free[0].first_name) + " will take care of your laundry")
        else:
            messages.info(
                request, "Sorry to say that. Our Staffs are currently busy.\nTry after some time")
        # form.save_m2m()
        return redirect('laundry:laundry')
    return render(request, 'laundry/booking.html', {'form': form})

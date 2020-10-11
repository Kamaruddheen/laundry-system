from usermodule.models import User
from django.shortcuts import get_object_or_404, render

from .models import *
from usermodule.decorators import user_is_staff
from django.utils.timezone import now, timedelta


@user_is_staff
def customer_list(request):
    customers = User.objects.filter(user_type=3)
    return render(request, 'customermodule/customer_list.html', {'customers': customers})


@user_is_staff
def customer_details(request, id):
    customer = get_object_or_404(User, id=id)
    status_time = (now() - timedelta(hours=24)
                   ) < (customer.last_login or (now() - timedelta(hours=24)))
    # 2020-10-11 15:40:43.624607+00:00 Now ==> now()
    # 2020-10-10 15:41:13.099188+00:00 after ==> now() - timedelta(hours=24)
    context = {'customer': customer, 'status_time': status_time}
    return render(request, 'customermodule/customer_detail.html', context)

from django.db import models
from usermodule.models import User
from staffmodule.models import *


class Booking(models.Model):
    cust_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cid")
    assigned_staff = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    sub_service = models.ForeignKey(
        Subservice, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    amount = models.FloatField(null=True, blank=True)
    delivery_choice = (('pickup', 'Pickup (Self)'), ('door-step', 'Door Step'))
    delivery_type = models.CharField(choices=delivery_choice, max_length=30)
    status_choice = (('New', 'New'), ('pending', 'Pending'), ('cleaning', 'Cleaning'), ('pickedup', 'Picked Up'), ('canceled', 'Canceled'),
                     ('ready', 'Ready'), ('delivered', 'Delivered'))
    status = models.CharField(max_length=20, choices=status_choice,
                              default=status_choice[0][0])
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.cust_id.last_name + ", " + self.cust_id.first_name


class Payment(models.Model):
    cust_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_mode_choice = (('cash', 'Cash'),
                           ('online', 'Online'))
    payment_mode = models.CharField(
        max_length=25, choices=payment_mode_choice, default=payment_mode_choice[0][0])
    paid_date = models.DateTimeField(auto_now_add=True)
    paid_amount = models.FloatField(null=True, blank=True)
    status_choice = (('paid', 'Paid'),
                     ('not_paid', 'Not Paid'))
    status = models.CharField(
        max_length=10, choices=status_choice, default=status_choice[1][0])

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

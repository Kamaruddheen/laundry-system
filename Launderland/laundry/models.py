from django.db import models
from usermodule.models import User
from staffmodule.models import Service


class Booking(models.Model):
    # which customer
    cust_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cid")
    # assigned to which staff
    assigned_staff = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    unit = models.PositiveIntegerField()
    delivery_choice = (('local', 'Pickup'), ('myself', 'Myself'))
    delivery_type = models.CharField(choices=delivery_choice, max_length=30)
    status_choice = (('pending', 'Pending'), ('pickedup', 'Picked Up'), ('canceled', 'Canceled'),
                     ('ready', 'Ready'), ('delivered', 'Delivered'))
    status = models.CharField(max_length=20, choices=status_choice,
                              default=status_choice[0][0])
    amount = models.FloatField(null=True, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    delivered_on = models.DateTimeField(null=True, blank=True)
    # address = models.CharField(User.address, max_length=100)
    # street = models.CharField(User.street, max_length=50)
    # city = models.CharField(User.city, max_length=50)
    # state = models.CharField(User.state, max_length=50)
    # pincode = models.CharField(User.pincode, max_length=6)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.cust_id.last_name + ", " + self.cust_id.first_name

from django.db import models
from usermodule.models import User
from staffmodule.models import Service


# class Booking(models.Model):
#     cid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cid")
#     staff = models.ForeignKey(User, on_delete=models.CASCADE)
#     services = models.ManyToManyField(Service)
#     service_on = models.DateField()
#     delivery_type = models.CharField(max_length=30,)
#     status_choice = (('pending', 'Pending'), ('pickedup', 'Picked Up'), ('canceled', 'Canceled'),
#                      ('ready', 'Ready'), ('delivered', 'Delivered'))
#     status = models.CharField(max_length=20, choices=status_choice,
#                               default=status_choice[0][0])
#     amount = models.FloatField(null=True, blank=True)
#     booked_on = models.DateTimeField(auto_now_add=True)
#     delivered_on = models.DateTimeField(null=True, blank=True)

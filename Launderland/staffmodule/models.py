from django.db import models
from django.db.models.deletion import CASCADE


class Service(models.Model):
    service = models.CharField(max_length=50)

    def __str__(self):
        return self.service


class Subservice(models.Model):
    sub_service = models.CharField(max_length=35)
    price = models.FloatField(max_length=5)
    service = models.ForeignKey(Service, on_delete=CASCADE)

    def __str__(self):
        return self.sub_service

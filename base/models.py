from django.db import models

# Create your models here.

class Flight(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    destination = models.CharField(max_length=200, null=True, blank=True)
    flight = models.CharField(max_length=200, null=True, blank=True)
    gate = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.destination


class Review(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Queue(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name




class Inventory(models.Model):
    class Meta:
        verbose_name_plural = "Inventories"
    storeid = models.CharField(max_length=200, null=True, blank=True)
    productid = models.CharField(max_length=200, null=True, blank=True)
    udpip = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=0)
    signal = models.BooleanField(default=False)

    def __str__(self):
        return self.storeid
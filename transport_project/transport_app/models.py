from django.db import models

class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.model} ({self.year})"

class Owner(models.Model):
    name = models.CharField(max_length=100)
    contact = models.EmailField()

    def __str__(self):
        return self.name

class Ownership(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.name} owns {self.vehicle.model}"
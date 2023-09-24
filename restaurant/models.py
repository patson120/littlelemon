from django.db import models

# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()



class MenuItem(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()


class Booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()
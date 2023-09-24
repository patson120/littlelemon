from django.db import models

# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()



class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True, default=0)
    inventory = models.SmallIntegerField(default=0)

    def get_items(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()
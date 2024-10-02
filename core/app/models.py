from django.db import models
import datetime


class Category(models.Model):
    title = models.CharField(max_length=223)

    def __str__(self):
        return self.title


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/cars_image')
    year = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=23, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(datetime.datetime.now())

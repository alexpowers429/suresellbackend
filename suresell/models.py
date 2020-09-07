from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Car(models.Model):
    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.year}, {self.make}, {self.model}, {self.trim}'


class SellingFeatures(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='features')
    feat1 = models.CharField(max_length=50)
    feat2 = models.CharField(max_length=50)
    feat3 = models.CharField(max_length=50)
    feat4 = models.CharField(max_length=50)
    feat5 = models.CharField(max_length=50)
    feat6 = models.CharField(max_length=50)
    feat7 = models.CharField(max_length=50)
    feat8 = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.feat1}, {self.feat2}, {self.feat3}, {self.feat4}, {self.feat4}, {self.feat5}, {self.feat6}, {self.feat7}, {self.feat8}'

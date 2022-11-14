
from django.db import models


# Create your models here.
class Address(models.Model):

    class Meta:
        tablename = 'address'
    
    street_1 = models.CharField(max_length=255, null=True, blank=True)
    street_2 = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    lat = models.DecimalField(null=True, blank=True)
    lon = models.DecimalField(null=True, blank=True)

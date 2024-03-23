from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(
        max_length=100, blank=True
    )
    last_name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone1 = models.CharField(max_length=30, blank=True)
    phone2 = models.CharField(max_length=30, blank=True)
    address1 = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254, blank=True)
    state_province = models.CharField(
        max_length=254, blank=True
    )
    zip_postal_code = models.CharField(
        max_length=20, blank=True
    )
    country = models.CharField(max_length=254, blank=True)

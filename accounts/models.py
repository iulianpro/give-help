from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=10, blank=False)
    town_city = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=False, default='')
    county = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' (' + self.user.profile.town_city + ')'

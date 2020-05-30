from django.db import models
from gifts.models import Gift
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=False, default='')
    country = models.CharField(max_length=40, blank=False, default='')
    postcode = models.CharField(max_length=20, blank=True, default='')
    town_or_city = models.CharField(max_length=40, blank=False, default='')
    street_address1 = models.CharField(max_length=40, blank=False, default='')
    street_address2 = models.CharField(max_length=40, blank=False, default='')
    county = models.CharField(max_length=40, blank=False, default='')
    date = models.DateField()

    def __str__(self):
        return "Order id {0} | {1} | {2}".format(self.id, self.full_name, self.date)


class Donate(models.Model):
    full_name = models.CharField(max_length=50, blank=False, default='')
    country = models.CharField(max_length=40, blank=False, default='')
    total = models.IntegerField(default=10, validators=[
                                MaxValueValidator(1000), MinValueValidator(10)])

    def __str__(self):
        return "{0} - {1} £".format(self.full_name, self.total)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    gift = models.ForeignKey(Gift, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} | {1} | {2}".format(
            self.quantity, self.gift.name, self.gift.price)

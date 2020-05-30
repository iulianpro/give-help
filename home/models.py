from django.db import models


class Galerry(models.Model):
    image = models.ImageField(upload_to="images")

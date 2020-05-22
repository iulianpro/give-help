from django.db import models


class GiftCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' (id: ' + self.id + ')'


class Gift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default="GBP")
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(
        "gifts.GiftCategory",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.name + ' (' + self.price + ' ' + self.currency + ' - ID: ' + self.id + ')'

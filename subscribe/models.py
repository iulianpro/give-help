from django.db import models


class Signup(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} | {1}".format(self.email, self.date)

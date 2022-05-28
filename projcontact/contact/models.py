from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

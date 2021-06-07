from django.db import models


# Create your models here.

class Stack(models.Model):
    name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name

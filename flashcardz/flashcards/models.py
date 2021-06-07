from django.db import models


class Card(models.Model):
    front = models.CharField(max_length=50, default=None)
    back = models.CharField(max_length=250, default=None)
    stack = models.ForeignKey('stacks.Stack', on_delete=models.CASCADE)

    def __str__(self):
        return self.front + self.back

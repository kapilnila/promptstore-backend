# Create your models here.
from django.db import models

class Prompt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    content = models.TextField()

    def __str__(self):
        return self.title

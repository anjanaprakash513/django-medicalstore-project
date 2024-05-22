from django.db import models

# Create your models here.
class medList(models.Model):
    Name = models.CharField(max_length=500)
    Form = models.CharField(max_length=500)
    Category = models.CharField(max_length=500)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
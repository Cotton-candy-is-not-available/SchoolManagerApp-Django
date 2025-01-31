from django.db import models

# Create your models here.

class Calendar(models.Model):
    year = models.DateField()
    month = models.DateField()
    day = models.DateField()
    day_number = models.IntegerField()





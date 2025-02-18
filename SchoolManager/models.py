from django.contrib.auth.models import User
from django.db import models

class TD_list(models.Model):
    List_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    def __str__(self):
        return self.List_name

class Task(models.Model):
    list = models.ForeignKey(TD_list, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    Important = models.BooleanField(default=False)
    mid_important = models.BooleanField(default=False)
    least_important = models.BooleanField(default=False)
    class Meta:
        ordering = ['-Important', '-mid_important', '-least_important']
    def __str__(self):
        return self.list.List_name + ": " + self.description




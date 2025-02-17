from django.db import models

class TD_list(models.Model):
    List_name = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.List_name

class Task(models.Model):
    list = models.ForeignKey(TD_list, on_delete=models.CASCADE)
    description = models.CharField(max_length=4096)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.list.List_name + ": " + self.description




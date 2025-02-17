from django.contrib import admin

# Register your models here.
from .models import TD_list, Task

admin.site.register(TD_list)
admin.site.register(Task)
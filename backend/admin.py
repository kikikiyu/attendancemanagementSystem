from django.contrib import admin
from  . import  models
admin.site.register(models.Employee)
admin.site.register(models.Attendance)
admin.site.register(models.Department)
admin.site.register(models.Overtime)
admin.site.register(models.Leave)

# Register your models here.

from django.contrib import admin
from .models import Employee, EmployeeRecord,PerformanceMetric,Task

admin.site.register(Employee)
admin.site.register(EmployeeRecord)
admin.site.register(PerformanceMetric)
admin.site.register(Task)

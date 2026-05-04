from django.contrib import admin

# Register your models here.

from app1.models import Employee

class Employee_admin(admin.ModelAdmin):
    
    list_display=['emp_id','emp_name','emp_sal']

admin.site.register(Employee,Employee_admin)

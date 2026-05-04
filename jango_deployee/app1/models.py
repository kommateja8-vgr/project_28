from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id= models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=50)
    emp_sal = models.FloatField()

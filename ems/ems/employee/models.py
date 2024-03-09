from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField("Name", max_length=100)
    employee_id = models.SmallIntegerField("Employee ID", unique=True)
    employee_hiredate = models.DateField("Employee Hire Date", null=True, blank=True)
    
    def __str__(self):
        return f"{self.employee_name} {self.employee_id}"

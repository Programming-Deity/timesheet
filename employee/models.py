from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=255)
    date_time_in = models.CharField(max_length=255)
    date_time_out = models.CharField(max_length=255)
    duration = models.FloatField()
    hourly_rate = models.FloatField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.emp_name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name
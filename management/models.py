from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    users = models.ManyToManyField('auth.User')  # or any user model you have
    platform_access = models.CharField(max_length=255)

    def __str__(self):
        return self.name

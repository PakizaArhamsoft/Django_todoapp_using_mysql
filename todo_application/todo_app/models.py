from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field import phonenumber

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.ForeignKey(User, null=True, related_name='parent_user', on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=200, null=False, blank=False)
    mobile = PhoneNumberField(blank=False, default="+12125552369", unique=True)
    # emp_code = models.BigAutoField(null=False, blank=False, default=1, unique=True)
    emp_code = models.IntegerField(null=False, blank=False, default=0, unique=True)
    # mobile = models.IntegerField(blank=False,default=1)
    is_removed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False)
    indexes = [models.Index(fields=['title'])]

    def __str__(self):
        ls = str(self.emp_name) + " ______ " + str(self.position)
        return ls



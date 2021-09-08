from django.db import models


class Employee(models.Model):
    first_name = models.CharField('Employee First Name', max_length=25)
    last_name = models.CharField('Employee Last Name', max_length=25)
    email = models.EmailField('Email')
    address = models.TextField('Address', null=True, blank=True)
    age = models.IntegerField('Age')
    city = models.CharField(max_length=35)

    def __str__(self):
        return str(self.email)

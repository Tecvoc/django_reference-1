from django.core.validators import MaxValueValidator
from django.db import models
from django.shortcuts import reverse


class Location(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    code = models.PositiveIntegerField(validators=[MaxValueValidator(limit_value=200)], unique=True)

    def __unicode__(self):
        return self.name + " in " + self.country


class Employee(models.Model):
    name = models.CharField(max_length=200)
    salary = models.PositiveIntegerField(validators=[MaxValueValidator(limit_value=9999999)],
                                         default=0)
    location = models.ForeignKey('Location', related_name="employees",
                                 to_field='code',
                                 on_delete=models.CASCADE,
                                 )

    @staticmethod
    def get_absolute_url():
        return reverse('myapp:employee_list')

    def __unicode__(self):
        return self.name

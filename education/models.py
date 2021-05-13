from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)

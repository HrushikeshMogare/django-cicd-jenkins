from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    date_hired = models.DateField()

    def __str__(self):
        return self.name
    





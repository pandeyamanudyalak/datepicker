from enum import auto
from django.db import models


# # Create your models here.
 

class Calender(models.Model):
    datefield = models.DateField()

    def __str__(self):
        return self.datefield




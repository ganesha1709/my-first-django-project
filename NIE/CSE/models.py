from django.db import models

# Create your models here.
class student(models.Model):
    name= models.CharField(max_length=30)
    dept= models.CharField(max_length=10)
    USN= models.IntegerField()
    def __str__(self):
        return self.name


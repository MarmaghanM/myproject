from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField('Student Name',max_length=20,blank=False,null=False)
    age = models.IntegerField('Student Age',null=False)
    address = models.TextField('Student Address')


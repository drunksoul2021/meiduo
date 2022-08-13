from django.db import models

# Create your models here.

class BookInfo(models.Model):
    #id The system will give to us id
    name=models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    #foreign key
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
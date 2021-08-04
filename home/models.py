from django.db import models

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=33)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Cakes(models.Model):
    name = models.CharField(max_length=33)
    number = models.IntegerField()
    desc = models.TextField()
    date = models.DateField()
       
    def __str__(self):
        return self.name


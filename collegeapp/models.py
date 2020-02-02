from django.db import models

# Create your models here.
#class Destination(models.Model):
 #   name = models.CharField(max_length=100)
  #  img = models.ImageField(upload_to='pics')
   # desc = models.TextField()
    #price = models.IntegerField()
    #offer = models.BooleanField(default=False)

class College(models.Model):
    department=models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    roll_no = models.CharField(max_length=150)
    game = models.CharField(max_length=150)
    section = models.CharField(max_length=150)
    def __str__(self):
        return self.name
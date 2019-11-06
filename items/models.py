from django.db import models

# Create your models here.

class Item(models.Model):
    title       = models.CharField(max_length=120, null=True, blank=True)
    price       = models.IntegerField( null=True, blank=True)
    quantity    = models.IntegerField(null=True, blank=True)
    image       = models.ImageField(null=True,blank=True)
    timestamp   = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True,auto_now_add=False)
    hostel      = models.CharField(default="BH-2" ,max_length=10,null=True,blank=True)
    i_type      = models.CharField(max_length=20,null=True,blank=True)
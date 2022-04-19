from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Theatre(models.Model):
    city_choice=(
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad'),
    )
    # name = models.CharField(max_length=50,null=False,default="Waves Cinema")
    city = models.CharField(max_length=9,choices=city_choice,null=False,unique=True)
    address = models.CharField(max_length=30)
    no_of_screen = models.IntegerField()

    def __str__(self):
        return self.city


class Movie_detail(models.Model):
    movie_name=models.CharField(max_length=100, blank=False, unique=False)
    movie_time=models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    city = models.ForeignKey(Theatre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s (Time:-%s)" % (self.movie_name, self.movie_time)
        
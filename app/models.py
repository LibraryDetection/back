from django.db import models


# Create your models here.
class Reservation(models.Model):
    seatNum  = models.CharField(max_length=5) #학번
    stuNum  = models.CharField(max_length=20) #학번


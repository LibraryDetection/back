from django.db import models


# Create your models here.
class Reservation(models.Model):
    seatNum  = models.CharField(max_length=5) #자리
    stuNum  = models.CharField(max_length=20) #학번

class DummyModel(models.Model):
    className = models.CharField(max_length=15, primary_key=True)
    classCount = models.IntegerField()
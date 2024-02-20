from django.db import models


# Create your models here.
class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    percentage_wins = models.IntegerField(default=0)

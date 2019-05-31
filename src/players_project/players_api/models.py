from django.db import models

# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    player_age = models.IntegerField(max_length=3)

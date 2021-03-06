from django.contrib.auth.models import User
from django.db import models
from plants.models import Seed

# Create your models here.
class Board(models.Model):
    objects = models.Manager()
    slot_1a = models.CharField(max_length=100, null=True)
    slot_1b = models.CharField(max_length=100, null=True)
    slot_1c = models.CharField(max_length=100, null=True)
    slot_1d = models.CharField(max_length=100, null=True)
    slot_1e = models.CharField(max_length=100, null=True)
    slot_1f = models.CharField(max_length=100, null=True)

    slot_2a = models.CharField(max_length=100, null=True)
    slot_2b = models.CharField(max_length=100, null=True)
    slot_2c = models.CharField(max_length=100, null=True)
    slot_2d = models.CharField(max_length=100, null=True)
    slot_2e = models.CharField(max_length=100, null=True)
    slot_2f = models.CharField(max_length=100, null=True)

    slot_3a = models.CharField(max_length=100, null=True)
    slot_3b = models.CharField(max_length=100, null=True)
    slot_3c = models.CharField(max_length=100, null=True)
    slot_3d = models.CharField(max_length=100, null=True)
    slot_3e = models.CharField(max_length=100, null=True)
    slot_3f = models.CharField(max_length=100, null=True)

    slot_4a = models.CharField(max_length=100, null=True)
    slot_4b = models.CharField(max_length=100, null=True)
    slot_4c = models.CharField(max_length=100, null=True)
    slot_4d = models.CharField(max_length=100, null=True)
    slot_4e = models.CharField(max_length=100, null=True)
    slot_4f = models.CharField(max_length=100, null=True)

    slot_5a = models.CharField(max_length=100, null=True)
    slot_5b = models.CharField(max_length=100, null=True)
    slot_5c = models.CharField(max_length=100, null=True)
    slot_5d = models.CharField(max_length=100, null=True)
    slot_5e = models.CharField(max_length=100, null=True)
    slot_5f = models.CharField(max_length=100, null=True)

    slot_6a = models.CharField(max_length=100, null=True)
    slot_6b = models.CharField(max_length=100, null=True)
    slot_6c = models.CharField(max_length=100, null=True)
    slot_6d = models.CharField(max_length=100, null=True)
    slot_6e = models.CharField(max_length=100, null=True)
    slot_6f = models.CharField(max_length=100, null=True)

    slot_7a = models.CharField(max_length=100, null=True)
    slot_7b = models.CharField(max_length=100, null=True)
    slot_7c = models.CharField(max_length=100, null=True)
    slot_7d = models.CharField(max_length=100, null=True)
    slot_7e = models.CharField(max_length=100, null=True)
    slot_7f = models.CharField(max_length=100, null=True)

    slot_8a = models.CharField(max_length=100, null=True)
    slot_8b = models.CharField(max_length=100, null=True)
    slot_8c = models.CharField(max_length=100, null=True)
    slot_8d = models.CharField(max_length=100, null=True)
    slot_8e = models.CharField(max_length=100, null=True)
    slot_8f = models.CharField(max_length=100, null=True)

    slot_9a = models.CharField(max_length=100, null=True)
    slot_9b = models.CharField(max_length=100, null=True)
    slot_9c = models.CharField(max_length=100, null=True)
    slot_9d = models.CharField(max_length=100, null=True)
    slot_9e = models.CharField(max_length=100, null=True)
    slot_9f = models.CharField(max_length=100, null=True)

    slot_10a = models.CharField(max_length=100, null=True)
    slot_10b = models.CharField(max_length=100, null=True)
    slot_10c = models.CharField(max_length=100, null=True)
    slot_10d = models.CharField(max_length=100, null=True)
    slot_10e = models.CharField(max_length=100, null=True)
    slot_10f = models.CharField(max_length=100, null=True)

    slot_11a = models.CharField(max_length=100, null=True)
    slot_11b = models.CharField(max_length=100, null=True)
    slot_11c = models.CharField(max_length=100, null=True)
    slot_11d = models.CharField(max_length=100, null=True)
    slot_11e = models.CharField(max_length=100, null=True)
    slot_11f = models.CharField(max_length=100, null=True)

    slot_12a = models.CharField(max_length=100, null=True)
    slot_12b = models.CharField(max_length=100, null=True)
    slot_12c = models.CharField(max_length=100, null=True)
    slot_12d = models.CharField(max_length=100, null=True)
    slot_12e = models.CharField(max_length=100, null=True)
    slot_12f = models.CharField(max_length=100, null=True)

class Round(models.Model):
    objects = models.Manager()

    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    winning_slot = models.CharField(max_length=10, blank=True, null=True)
    winning_seed = models.CharField(max_length=100, blank=True, null=True)
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
    lock_time = models.DateTimeField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class ScoreBoard(models.Model):
    objects = models.Manager()

    round = models.ForeignKey(Round, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    slot_choice = models.CharField(max_length=10, null=True)
    seed_choice = models.CharField(max_length=100, null=True)
    win_status = models.NullBooleanField()

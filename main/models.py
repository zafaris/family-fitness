from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


# Create your models here.
class FitnessRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class CategoryChoices(models.TextChoices):
        BIKE = 'Bike'
        WALK = 'Walk'
        RUN = 'Run'
        SPORTS = 'Sports'

    category = models.CharField(max_length=10, choices=CategoryChoices.choices, default=CategoryChoices.BIKE)

    calories = models.IntegerField(default=100)
    duration = models.DurationField(default='00:30:00', help_text='HH:MM:ss format')

    def __str__(self):
        return f'{self.user.username} | {self.category} | {self.calories}'

def generateCode():
    return get_random_string(length=6)

class Family(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(User)
    code = models.CharField(max_length=6, default=generateCode, unique=True)

    class Meta:
        verbose_name_plural = 'Families'
    
    def __str__(self):
        return f'{self.name} | {self.members.all().count()} members | {self.code}'

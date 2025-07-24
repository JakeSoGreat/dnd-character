from django.db import models
from django.contrib.auth.models import User

# Race model
class Race(models.Model):
    name = models.CharField(max_length=100)
    traits = models.TextField()

    def __str__(self):
        return self.name

# Background model
class Background(models.Model):
    name = models.CharField(max_length=100)
    skill_proficiency = models.CharField(max_length=200)
    tool_proficiency = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Alignment model
class Alignment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Character model
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='character_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    level = models.PositiveIntegerField(default=1)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    background = models.ForeignKey(Background, on_delete=models.SET_NULL, null=True)
    alignment = models.ForeignKey(Alignment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
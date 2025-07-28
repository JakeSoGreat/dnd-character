from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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


# Class model (D&D character classes)
class Class(models.Model):
    name = models.CharField(max_length=100)
    features = models.TextField()

    def __str__(self):
        return self.name


# Spells model
class Spell(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=50)
    level = models.PositiveIntegerField(
        choices=[(0, "Cantrip")] + [(i, str(i)) for i in range(1, 10)]
    )

    def __str__(self):
        return f"{self.name} (Level {self.level})"


# Items model
class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Feats model
class Feat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    prerequisite = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


# Character model
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    level = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    background = models.ForeignKey(
        Background, on_delete=models.SET_NULL, null=True
    )
    alignment = models.ForeignKey(
        Alignment, on_delete=models.SET_NULL, null=True
    )
    
    strength = models.PositiveIntegerField(default=10)
    dexterity = models.PositiveIntegerField(default=10)
    constitution = models.PositiveIntegerField(default=10)
    intelligence = models.PositiveIntegerField(default=10)
    wisdom = models.PositiveIntegerField(default=10)
    charisma = models.PositiveIntegerField(default=10)
    
    # Many-to-many relationships
    character_classes = models.ManyToManyField(Class, blank=True)
    spells = models.ManyToManyField(Spell, blank=True)
    items = models.ManyToManyField(Item, blank=True)
    feats = models.ManyToManyField(Feat, blank=True)

    def __str__(self):
        return self.name



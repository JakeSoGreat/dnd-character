from django.contrib import admin
from .models import (
    Race, Background, Alignment, Character, 
    CharacterClass, Spell, Item, Feat, AbilityScore
)

admin.site.register(Race)
admin.site.register(Background)
admin.site.register(Alignment)
admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(Spell)
admin.site.register(Item)
admin.site.register(Feat)
admin.site.register(AbilityScore)

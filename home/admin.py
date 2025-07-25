from django.contrib import admin
from .models import (
    Race, Background, Alignment, Character, 
    Class, Spell, Item, Feat
)

admin.site.register(Race)
admin.site.register(Background)
admin.site.register(Alignment)
admin.site.register(Character)
admin.site.register(Class)
admin.site.register(Spell)
admin.site.register(Item)
admin.site.register(Feat)

from django import forms
from .models import Character, Class, Spell, Item, Feat


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'description', 'level', 'race', 'background', 'alignment',
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
            'character_classes', 'spells', 'items', 'feats'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'race': forms.Select(attrs={'class': 'form-control'}),
            'background': forms.Select(attrs={'class': 'form-control'}),
            'alignment': forms.Select(attrs={'class': 'form-control'}),
            'strength': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'dexterity': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'constitution': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'intelligence': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'wisdom': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'charisma': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'character_classes': forms.CheckboxSelectMultiple(),
            'spells': forms.CheckboxSelectMultiple(),
            'items': forms.CheckboxSelectMultiple(),
            'feats': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make many-to-many fields optional
        self.fields['character_classes'].required = True
        self.fields['spells'].required = False
        self.fields['items'].required = False
        self.fields['feats'].required = True
        
        # Add help text
        self.fields['character_classes'].help_text = "Select character classes"
        self.fields['spells'].help_text = "Select known spells"
        self.fields['items'].help_text = "Select carried items"
        self.fields['feats'].help_text = "Select character feats"


# Quick-add forms for new spells and items only
class QuickSpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = ['name', 'school', 'level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spell name'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Evocation'}),
            'level': forms.Select(attrs={'class': 'form-control'})
        }


class QuickItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item name'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Weapon, Armor'})
        }

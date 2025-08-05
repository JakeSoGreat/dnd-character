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
            'character_classes': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
            'spells': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
            'items': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
            'feats': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['character_classes'].required = True
        self.fields['spells'].required = False
        self.fields['items'].required = False
        self.fields['feats'].required = False
        self.fields['character_classes'].help_text = "Hold Ctrl (Cmd on Mac) to select multiple classes"
        self.fields['spells'].help_text = "Hold Ctrl (Cmd on Mac) to select multiple spells"
        self.fields['items'].help_text = "Hold Ctrl (Cmd on Mac) to select multiple items"
        self.fields['feats'].help_text = "Hold Ctrl (Cmd on Mac) to select multiple feats"

    def clean_level(self):
        level = self.cleaned_data.get('level')
        if level is not None:
            if level > 20:
                raise forms.ValidationError("Character level cannot be higher than 20.")
            if level < 1:
                raise forms.ValidationError("Character level cannot be lower than 1.")
        return level


# Quick-add forms for new spells and items
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

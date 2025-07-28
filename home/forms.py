from django import forms
from .models import Character, Class, Spell, Item


class CharacterForm(forms.ModelForm):
    # Many-to-many fields for existing data
    classes = forms.ModelMultipleChoiceField(
        queryset=Class.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select existing classes"
    )
    spells = forms.ModelMultipleChoiceField(
        queryset=Spell.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select existing spells"
    )
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select existing items"
    )

    class Meta:
        model = Character
        fields = [
            'name', 'description', 'level', 'race', 'background', 'alignment',
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
            'classes', 'spells', 'items'
        ]
        widgets = {
            'strength': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'dexterity': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'constitution': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'intelligence': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'wisdom': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
            'charisma': forms.NumberInput(attrs={'min': 1, 'max': 20, 'class': 'form-control'}),
        }


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

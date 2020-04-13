# part/forms.py
from django import forms
from .models import Item, Item_part

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'ident',)

class Item_partForm(forms.ModelForm):

    class Meta:
        model = Item_part
        fields = ('name', 'number', 'notes',)







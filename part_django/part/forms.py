# part/forms.py
from django import forms
from .models import Item, Item_part

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'ident',)







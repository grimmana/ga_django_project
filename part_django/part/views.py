from django.shortcuts import render
from .models import Item, Item_part
# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'part/item_list.html', {'items': items})

def item_part_list(request):
    item_parts = Item_part.objects.all()
    return render(request, 'part/item_part_list.html', {'item_parts': item_parts})

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'part/item_detail.html', {'item': item})

def item_part_detail(request, pk):
    item_part = Item_part.objects.get(id=pk)
    return render(request, 'part/item_part_detail.html', {'item_part': item_part})    
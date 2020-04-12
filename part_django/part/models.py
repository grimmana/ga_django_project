from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    ident = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item_part(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_parts')
    part_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100) 
    part_notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name
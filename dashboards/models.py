from django.db import models

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag', related_name='items')
    stock_status = models.CharField(max_length=50)
    available_stock = models.IntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
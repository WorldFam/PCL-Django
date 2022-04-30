from django.db import models

class Drink(models.Model):

    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    DRINK_SIZE = [
        (SMALL,'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    name = models.CharField(max_length=20, default='')
    size = models.CharField(max_length=10, choices= DRINK_SIZE, default= SMALL)
    price = models.FloatField()
    category = models.ForeignKey('Category',related_name='category',on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    price = models.FloatField(default=0.0)
    items = models.ManyToManyField('Drink', related_name='order', blank=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'


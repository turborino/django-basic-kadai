from django.db import models
from django.forms import widgets
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Detail(models.Model):
    detail = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.detail

class Product(models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')
    
    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('list')
    

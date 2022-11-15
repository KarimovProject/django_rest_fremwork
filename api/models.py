from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ram = models.IntegerField()
    memory = models.IntegerField()
    price = models.FloatField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

# Модель покупателя
class Buyer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.username

# Модель игры
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
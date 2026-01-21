from django.db import models

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=200)

    price = models.PositiveIntegerField()

    CATEGORY_OPTIONS= (
        ("mens","mens"),
        ("womens","womens"),
        ("kids","kids")
    )

    category = models.CharField(max_length=200,choices=CATEGORY_OPTIONS,default="mens")

    size=models.CharField(max_length=20)

    brand=models.CharField(max_length=200)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class products(models.Model):

    name = models.CharField(unique=True,max_length=128)

    price = models.PositiveIntegerField()

    picture = models.ImageField(upload_to='product_img')

    id = models.CharField(unique=True,primary_key=True,max_length=10)

from django.db import models
from core.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Favorites(models.Model):
    favorite_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.favorite_code)
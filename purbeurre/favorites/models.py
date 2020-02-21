from django.db import models
from core.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Favorites(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)

    @staticmethod
    def is_favorite(product, user):
        return Favorites.objects.filter(product=product, user=user).exists()
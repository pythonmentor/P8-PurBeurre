from django.db import models

# Create your models here.


class Favorites(models.Model):
    product_code = models.BigIntegerField(primary_key=True)

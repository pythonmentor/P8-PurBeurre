from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=20)


class Product(models.Model):
    # product_code pk
    product_code = models.BigIntegerField(primary_key=True)
    # name
    product_name = models.CharField(max_length=50)
    # category_id
    product_category_id = models.PositiveSmallIntegerField()
    # nutriscore
    product_nutriscore = models.CharField(max_length=1)
    # urlimage
    product_image_url = models.URLField(max_length=200)    
    # link
    product_url = models.URLField(max_length=200)

    # nutriments_100g VITAMINS ??
    product_energy_kcal_100g = models.CharField(max_length=10)
    product_fat_100g = models.CharField(max_length=10)
    product_saturated_fat_100g = models.CharField(max_length=10)
    product_salt_100g = models.CharField(max_length=10)
    product_carbohydrates_100g = models.CharField(max_length=10)
    product_fibers_100g = models.CharField(max_length=10)
    product_sugars_100g = models.CharField(max_length=10)
    product_proteins_100g = models.CharField(max_length=10)

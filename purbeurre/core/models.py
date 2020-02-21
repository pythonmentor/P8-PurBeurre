from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class UserRegistrationForm(UserCreationForm):
    email = forms.email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #help_texts = {
        #    'username': ''
        #}


class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)


class Product(models.Model):
    product_code = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=150)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_nutriscore = models.CharField(max_length=3)
    product_image_url = models.URLField(max_length=200)
    product_url = models.URLField(max_length=200)

    # nutriments_100g
    product_energy_kj_100g = models.CharField(max_length=20)
    product_fat_100g = models.CharField(max_length=20)
    product_saturated_fat_100g = models.CharField(max_length=20)
    product_salt_100g = models.CharField(max_length=20)
    product_carbohydrates_100g = models.CharField(max_length=20)
    product_fibers_100g = models.CharField(max_length=20)
    product_sugars_100g = models.CharField(max_length=20)
    product_proteins_100g = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name
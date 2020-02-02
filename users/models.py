from django.db import models

# Create your models here.


class userdata(models.Model):
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=64)

# Generated by Django 3.0.2 on 2020-02-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200203_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]

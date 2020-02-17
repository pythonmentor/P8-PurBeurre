# Generated by Django 3.0.2 on 2020-02-16 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20200204_2335'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0002_delete_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-29 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
            preserve_default=False,
        ),
    ]

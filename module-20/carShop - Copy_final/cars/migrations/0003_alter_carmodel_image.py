# Generated by Django 5.0.6 on 2024-07-25 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_imgage_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, default='cars/media/upload/home.webp', null=True, upload_to='cars/media/upload'),
        ),
    ]
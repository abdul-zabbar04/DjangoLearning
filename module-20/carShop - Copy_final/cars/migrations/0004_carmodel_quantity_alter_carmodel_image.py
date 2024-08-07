# Generated by Django 5.0.6 on 2024-07-26 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, default='cars/upload/home.webp', null=True, upload_to='cars/upload'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
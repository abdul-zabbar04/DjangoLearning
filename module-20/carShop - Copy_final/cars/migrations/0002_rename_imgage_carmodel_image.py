# Generated by Django 5.0.6 on 2024-07-22 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='imgage',
            new_name='image',
        ),
    ]

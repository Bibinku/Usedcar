# Generated by Django 5.0.4 on 2024-05-08 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardb',
            old_name='number',
            new_name='model',
        ),
    ]

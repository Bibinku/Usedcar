# Generated by Django 5.0.4 on 2024-08-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0006_remove_branddb_bmodel_remove_branddb_bname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardb',
            name='gst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cardb',
            name='insurance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

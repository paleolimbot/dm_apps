# Generated by Django 2.1.4 on 2019-05-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0028_surface_is_lost'),
    ]

    operations = [
        migrations.AddField(
            model_name='surface',
            name='old_plateheader_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
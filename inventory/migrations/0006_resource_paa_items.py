# Generated by Django 2.2.2 on 2020-05-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_models', '0003_paaitem'),
        ('inventory', '0005_auto_20200507_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='paa_items',
            field=models.ManyToManyField(blank=True, to='shared_models.PAAItem'),
        ),
    ]

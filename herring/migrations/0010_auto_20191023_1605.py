# Generated by Django 2.2.2 on 2019-10-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herring', '0009_auto_20191017_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meshsize',
            name='size_mm',
            field=models.IntegerField(null=True),
        ),
    ]
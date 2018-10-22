# Generated by Django 2.0.4 on 2018-10-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herring', '0040_auto_20181018_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='latitude_n',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude (N)'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='longitude_w',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude (W)'),
        ),
    ]
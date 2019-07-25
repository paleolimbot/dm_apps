# Generated by Django 2.2.2 on 2019-07-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0070_auto_20190725_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='depth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='depth'),
        ),
        migrations.AlterField(
            model_name='site',
            name='lat',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='latitude N (DD.dddddd)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='long',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='longitude W (DD.dddddd)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=255, verbose_name='site name'),
        ),
        migrations.AlterField(
            model_name='site',
            name='substrate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='substrate'),
        ),
        migrations.AlterField(
            model_name='site',
            name='width',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='width'),
        ),
    ]

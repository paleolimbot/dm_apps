# Generated by Django 2.0.4 on 2018-11-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0022_auto_20181121_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentalreport',
            name='species',
            field=models.ManyToManyField(to='grais.Species', verbose_name='Concerning which species'),
        ),
    ]
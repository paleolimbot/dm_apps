# Generated by Django 2.1.4 on 2019-03-26 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prey',
            name='length_is_approximation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='predator',
            name='processing_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='processing date'),
        ),
    ]
# Generated by Django 2.0.4 on 2018-11-28 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowcrab', '0004_auto_20181128_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crab',
            name='egg_colour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crab',
            name='gonad_colour',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
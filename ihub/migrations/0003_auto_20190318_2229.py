# Generated by Django 2.1.4 on 2019-03-19 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihub', '0002_auto_20190318_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='regions',
            field=models.ManyToManyField(related_name='entries', to='shared_models.Region'),
        ),
    ]
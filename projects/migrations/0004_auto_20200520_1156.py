# Generated by Django 2.2.2 on 2020-05-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200520_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
    ]

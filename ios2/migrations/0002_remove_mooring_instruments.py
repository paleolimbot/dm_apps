# Generated by Django 2.1.4 on 2019-04-05 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mooring',
            name='instruments',
        ),
    ]

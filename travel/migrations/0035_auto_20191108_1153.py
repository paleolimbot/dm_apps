# Generated by Django 2.2.2 on 2019-11-08 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0034_auto_20191108_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='total_non_dfo_cost',
            new_name='non_dfo_costs',
        ),
    ]
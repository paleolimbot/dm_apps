# Generated by Django 2.0.7 on 2018-11-05 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0006_auto_20181102_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidentalreport',
            old_name='date_created',
            new_name='report_date',
        ),
    ]
# Generated by Django 2.0.4 on 2018-11-06 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0008_auto_20181105_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidentalreport',
            options={'ordering': ['-report_date']},
        ),
    ]
# Generated by Django 2.0.7 on 2018-11-02 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grais', '0003_auto_20181102_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentalreport',
            name='report_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 2.0.4 on 2018-07-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 2.2.2 on 2019-07-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trapnet', '0029_auto_20190718_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='abbrev',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='abbreviation'),
        ),
    ]

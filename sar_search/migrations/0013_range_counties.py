# Generated by Django 2.2.2 on 2019-07-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0012_auto_20190731_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='counties',
            field=models.ManyToManyField(blank=True, to='sar_search.County'),
        ),
    ]

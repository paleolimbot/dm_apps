# Generated by Django 2.2.2 on 2020-03-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0003_merge_20200110_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='test',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
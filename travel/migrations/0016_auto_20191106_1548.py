# Generated by Django 2.2.2 on 2019-11-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0015_auto_20191106_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='parent_event',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

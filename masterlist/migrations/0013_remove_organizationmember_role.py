# Generated by Django 2.1.4 on 2019-05-07 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0012_auto_20190507_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationmember',
            name='role',
        ),
    ]

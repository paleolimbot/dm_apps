# Generated by Django 2.1.4 on 2019-03-14 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_event_funding_source'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_date', 'last_name']},
        ),
    ]

# Generated by Django 2.2.2 on 2019-12-11 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0014_auto_20191211_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='species',
            old_name='notes',
            new_name='notes_eng',
        ),
    ]

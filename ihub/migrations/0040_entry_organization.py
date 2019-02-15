# Generated by Django 2.1.4 on 2019-02-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihub', '0039_remove_entry_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='organization',
            field=models.ManyToManyField(related_name='entries', to='ihub.Organization'),
        ),
    ]
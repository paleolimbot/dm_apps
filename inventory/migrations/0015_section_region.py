# Generated by Django 2.1.4 on 2019-01-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_resource_data_management_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='region',
            field=models.IntegerField(choices=[(1, 'Gulf'), (2, 'Maritime'), (3, 'Quebec'), (4, 'Central & Arctic'), (5, 'Pacific'), (6, 'Newfoundland and Labrador')], default=1),
            preserve_default=False,
        ),
    ]
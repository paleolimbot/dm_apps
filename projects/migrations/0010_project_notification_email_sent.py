# Generated by Django 2.2.2 on 2020-05-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_allocated_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='notification_email_sent',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Notification Email Sent'),
        ),
    ]

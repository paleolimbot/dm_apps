# Generated by Django 2.2.2 on 2019-09-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_helptext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helptext',
            name='fra_text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
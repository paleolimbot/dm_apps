# Generated by Django 2.2.2 on 2020-05-14 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20200513_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

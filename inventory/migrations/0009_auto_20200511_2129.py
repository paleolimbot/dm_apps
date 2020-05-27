# Generated by Django 2.2.2 on 2020-05-12 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200508_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='od_release_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date released to Open Gov't Portal"),
        ),
        migrations.AlterField(
            model_name='resource',
            name='od_publication_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date published to Open Gov't Portal"),
        ),
    ]

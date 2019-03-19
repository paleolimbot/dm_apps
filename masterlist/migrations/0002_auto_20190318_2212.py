# Generated by Django 2.1.4 on 2019-03-19 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Province', verbose_name='province'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='regions',
            field=models.ManyToManyField(blank=True, to='shared_models.Region', verbose_name='region'),
        ),
    ]

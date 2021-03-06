# Generated by Django 2.2.2 on 2019-10-04 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20190628_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Point order')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.GeographicScope', verbose_name='Polygon Name')),
            ],
        ),
    ]

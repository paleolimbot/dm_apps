# Generated by Django 2.1.4 on 2019-04-09 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ios2', '0002_auto_20190409_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicehistory',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='ios2.Instrument', verbose_name='instrument'),
        ),
    ]
# Generated by Django 2.2.2 on 2020-03-23 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whalesdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edaequipmentattachment',
            name='eqp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='equipment', to='whalesdb.EqpEquipment', verbose_name='Equipment'),
        ),
    ]

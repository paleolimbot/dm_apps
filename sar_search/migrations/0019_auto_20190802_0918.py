# Generated by Django 2.2.2 on 2019-08-02 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0018_auto_20190802_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='range_type',
            new_name='record_type',
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=255, verbose_name='record name'),
        ),
        migrations.AlterField(
            model_name='record',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='records', to='sar_search.Species'),
        ),
    ]
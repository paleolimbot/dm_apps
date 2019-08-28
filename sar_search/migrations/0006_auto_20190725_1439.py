# Generated by Django 2.2.2 on 2019-07-25 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sar_search', '0005_auto_20190725_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='aphia_id',
        ),
        migrations.RemoveField(
            model_name='species',
            name='code',
        ),
        migrations.AlterField(
            model_name='species',
            name='common_name_eng',
            field=models.CharField(max_length=255, verbose_name='name (English)'),
        ),
        migrations.AlterField(
            model_name='species',
            name='cosewic_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cosewic_spp', to='sar_search.SpeciesStatus', verbose_name='SARA status'),
        ),
        migrations.AlterField(
            model_name='species',
            name='province_range',
            field=models.ManyToManyField(blank=True, to='shared_models.Province'),
        ),
        migrations.AlterField(
            model_name='species',
            name='sara_schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='spp', to='sar_search.SARASchedule', verbose_name='SARA schedule'),
        ),
        migrations.AlterField(
            model_name='species',
            name='sara_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sara_spp', to='sar_search.SpeciesStatus', verbose_name='COSEWIC status'),
        ),
        migrations.AlterField(
            model_name='species',
            name='taxon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='spp', to='sar_search.Taxon'),
        ),
    ]
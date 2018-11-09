# Generated by Django 2.0.4 on 2018-11-08 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_eng', models.CharField(blank=True, max_length=255, null=True)),
                ('province_fre', models.CharField(blank=True, max_length=255, null=True)),
                ('abbrev_eng', models.CharField(blank=True, max_length=10, null=True)),
                ('abbrev_fre', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_start_date', models.DateTimeField(blank=True, null=True)),
                ('sample_end_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='camp_sample_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sample_start_date'],
            },
        ),
        migrations.CreateModel(
            name='SampleSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sample_spp', to='camp.Sample')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_eng', models.CharField(blank=True, max_length=255, null=True)),
                ('site_fre', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sites', to='camp.Province')),
            ],
            options={
                'ordering': ['province', 'site_eng'],
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name_eng', models.CharField(blank=True, max_length=255, null=True)),
                ('common_name_fre', models.CharField(blank=True, max_length=255, null=True)),
                ('scientific_name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('tsn', models.IntegerField(blank=True, null=True, verbose_name='ITIS TSN')),
                ('aphia_id', models.IntegerField(blank=True, null=True, verbose_name='AphiaID')),
            ],
            options={
                'ordering': ['common_name_eng'],
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=5)),
                ('desc_eng', models.TextField(max_length=5)),
                ('desc_fre', models.TextField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude_n', models.FloatField(blank=True, null=True)),
                ('longitude_w', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stations', to='camp.Site')),
            ],
        ),
        migrations.AddField(
            model_name='samplespecies',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sample_spp', to='camp.Species'),
        ),
        migrations.AddField(
            model_name='samplespecies',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sample_spp', to='camp.Stage'),
        ),
        migrations.AddField(
            model_name='sample',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='samples', to='camp.Station'),
        ),
    ]
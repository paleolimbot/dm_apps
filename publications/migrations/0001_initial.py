# Generated by Django 2.1.4 on 2019-05-16 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_models', '0013_language'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EcosystemComponents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HumanComponents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramLinkage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_year', models.DateField(verbose_name='Publication Year')),
                ('pub_title', models.CharField(max_length=255, verbose_name='Publication Title')),
                ('date_last_modified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date last modified')),
                ('pub_abstract', models.TextField(blank=True, null=True, verbose_name='Abstract')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Division', verbose_name='Division')),
                ('ecosystem_component', models.ManyToManyField(to='publications.EcosystemComponents', verbose_name='Ecosystem Component(s)')),
                ('human_component', models.ManyToManyField(to='publications.HumanComponents', verbose_name='Human Component(s)')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('program_linkage', models.ManyToManyField(to='publications.ProgramLinkage', verbose_name='Program Linkage(s)')),
            ],
            options={
                'ordering': ['-pub_year', 'division', 'pub_title'],
            },
        ),
        migrations.CreateModel(
            name='SpatialManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SustainabilityPillar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='publications',
            name='spatial_management',
            field=models.ManyToManyField(to='publications.SpatialManagement', verbose_name='Spatial Management Designation(s)'),
        ),
        migrations.AddField(
            model_name='publications',
            name='sustainability_pillar',
            field=models.ManyToManyField(to='publications.SustainabilityPillar', verbose_name='Pillar(s) of Sustainability'),
        ),
        migrations.AddField(
            model_name='publications',
            name='theme',
            field=models.ManyToManyField(to='publications.Theme', verbose_name='Theme(s)'),
        ),
    ]

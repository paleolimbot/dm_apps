# Generated by Django 2.2.2 on 2019-06-27 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_models', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EcosystemComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Ecosystem Component',
                'verbose_name_plural': 'Ecosystem Component(s)',
            },
        ),
        migrations.CreateModel(
            name='GeoCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('north_south', models.FloatField()),
                ('east_west', models.FloatField()),
            ],
            options={
                'verbose_name': 'Geographic Coordinate',
                'verbose_name_plural': 'Geographic Coordinates',
            },
        ),
        migrations.CreateModel(
            name='GeographicScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Geographic Scope',
                'verbose_name_plural': 'Geographic Scope(s)',
            },
        ),
        migrations.CreateModel(
            name='HumanComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Human Component',
                'verbose_name_plural': 'Human Component(s)',
            },
        ),
        migrations.CreateModel(
            name='InternalContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Contact (Internal)',
                'verbose_name_plural': 'Contact(s) (Internal)',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organization(s)',
            },
        ),
        migrations.CreateModel(
            name='Pillar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Pillar of Sustainability',
                'verbose_name_plural': 'Pillar(s) of Sustainability',
            },
        ),
        migrations.CreateModel(
            name='ProgramLinkage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Linkage to Program',
                'verbose_name_plural': 'Linkage(s) to Program',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Project Title')),
                ('year', models.IntegerField(default=0)),
                ('date_last_modified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date last modified')),
                ('abstract', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('method', models.TextField(blank=True, null=True, verbose_name='Method')),
                ('coordinates', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='publications.GeoCoordinate', verbose_name='Coordinate(s)')),
                ('dfo_contact', models.ManyToManyField(to='publications.InternalContact', verbose_name='Contact(s) (Internal)')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shared_models.Division', verbose_name='Division')),
                ('ecosystem_component', models.ManyToManyField(to='publications.EcosystemComponent', verbose_name='Ecosystem Component(s)')),
                ('geographic_scope', models.ManyToManyField(to='publications.GeographicScope', verbose_name='Geographic Scope(s)')),
                ('human_component', models.ManyToManyField(to='publications.HumanComponent', verbose_name='Human Component(s)')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pub_projects', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ManyToManyField(to='publications.Organization', verbose_name='Organization(s)')),
                ('program_linkage', models.ManyToManyField(to='publications.ProgramLinkage', verbose_name='Program Linkage(s)')),
            ],
            options={
                'ordering': ['title', 'division'],
            },
        ),
        migrations.CreateModel(
            name='SpatialScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Spatial Scale',
                'verbose_name_plural': 'Spatial Scale(s)',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Theme(s)',
            },
        ),
        migrations.CreateModel(
            name='SpatialManagementDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Spatial Management Designation',
                'verbose_name_plural': 'Spatial Management Designation(s)',
            },
        ),
        migrations.CreateModel(
            name='SpatialDataProductYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Spatial Data Product Year',
                'verbose_name_plural': 'Spatial Data Product Year(s)',
            },
        ),
        migrations.CreateModel(
            name='SpatialDataProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Spatial Data Product',
                'verbose_name_plural': 'Spatial Data Product(s)',
            },
        ),
        migrations.CreateModel(
            name='SourceDataInternal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Data Source (Internal)',
                'verbose_name_plural': 'Data Source(s) (Internal)',
            },
        ),
        migrations.CreateModel(
            name='SourceDataExternal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Data Source (External)',
                'verbose_name_plural': 'Data Source(s) (External)',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Site(s)',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publication(s)',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='spatial_scale',
            field=models.ManyToManyField(to='publications.SpatialScale', verbose_name='Spatial Scale(s)'),
        ),
        migrations.AddField(
            model_name='project',
            name='sustainability_pillar',
            field=models.ManyToManyField(to='publications.Pillar', verbose_name='Pillar(s) of Sustainability'),
        ),
        migrations.AddField(
            model_name='project',
            name='theme',
            field=models.ManyToManyField(to='publications.Theme', verbose_name='Theme(s)'),
        ),
        migrations.CreateModel(
            name='FgpLinkage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'FGP Linkage',
                'verbose_name_plural': 'FGP Linkage(s)',
            },
        ),
        migrations.CreateModel(
            name='ExternalContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Contact (External)',
                'verbose_name_plural': 'Contact(s) (External)',
            },
        ),
        migrations.CreateModel(
            name='ComputerLibraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Computer Library',
                'verbose_name_plural': 'Computer Libraries',
            },
        ),
        migrations.CreateModel(
            name='ComputerEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Computer Environment',
                'verbose_name_plural': 'Computer Environment(s)',
            },
        ),
        migrations.CreateModel(
            name='CodeSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Code Site',
                'verbose_name_plural': 'Code Site(s)',
            },
        ),
    ]

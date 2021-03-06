# Generated by Django 2.2.2 on 2020-07-21 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ihub.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared_models', '0007_auto_20200617_0856'),
        ('ihub', '0002_auto_20200706_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name (English)')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name (French)')),
                ('is_indigenous', models.BooleanField(default=False, verbose_name='indigenous?')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_eng', models.CharField(max_length=1000, verbose_name='legal name')),
                ('name_ind', models.CharField(blank=True, max_length=1000, null=True, verbose_name='indigenous Name')),
                ('abbrev', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='abbreviation')),
                ('address', models.CharField(blank=True, max_length=1000, null=True, verbose_name='street address')),
                ('mailing_address', models.CharField(blank=True, max_length=1000, null=True, verbose_name='mailing address')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='city')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='postal code')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='phone')),
                ('fax', models.CharField(blank=True, max_length=100, null=True, verbose_name='fax')),
                ('dfo_contact_instructions', models.TextField(blank=True, null=True, verbose_name='DFO contact instructions')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('consultation_protocol', models.TextField(blank=True, null=True, verbose_name='consultation protocol')),
                ('key_species', models.TextField(blank=True, null=True, verbose_name='key species')),
                ('former_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='former name')),
                ('website', models.URLField(blank=True, null=True, verbose_name='website')),
                ('council_quorum', models.IntegerField(blank=True, null=True, verbose_name='council quorum')),
                ('next_election', models.DateTimeField(blank=True, max_length=100, null=True, verbose_name='next election')),
                ('election_term', models.CharField(blank=True, max_length=100, null=True, verbose_name='election term')),
                ('new_coucil_effective_date', models.DateTimeField(blank=True, null=True, verbose_name='date that the new council holds office')),
                ('population_on_reserve', models.IntegerField(blank=True, null=True, verbose_name='population on reserve')),
                ('population_off_reserve', models.IntegerField(blank=True, null=True, verbose_name='population off reserve')),
                ('population_other_reserve', models.IntegerField(blank=True, null=True, verbose_name='population on other reserve')),
                ('fin', models.CharField(blank=True, max_length=100, null=True, verbose_name='FIN')),
                ('processing_plant', models.IntegerField(choices=[(0, 'None'), (1, 'On-Reserve'), (2, 'Off-Reserve'), (3, 'Both')], default=0, verbose_name='processing plant?')),
                ('wharf', models.IntegerField(choices=[(0, 'None'), (1, 'On-Reserve'), (2, 'Off-Reserve'), (3, 'Both')], default=0, verbose_name='wharf?')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=ihub.models.audio_file_directory_path, verbose_name='audio file')),
                ('date_last_modified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date last modified')),
                ('old_id', models.IntegerField(blank=True, null=True)),
                ('grouping', models.ManyToManyField(blank=True, to='ihub.Grouping', verbose_name='grouping')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='x1', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
                ('nation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ihub.Nation', verbose_name='Nation')),
                ('orgs', models.ManyToManyField(blank=True, limit_choices_to={'grouping__is_indigenous': 1}, related_name='org1', to='ihub.Organization', verbose_name='Associated organizations')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delete123', to='shared_models.Province', verbose_name='province')),
                ('regions', models.ManyToManyField(blank=True, related_name='delete123', to='shared_models.Region', verbose_name='region')),
            ],
            options={
                'ordering': ['name_eng'],
            },
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=500, null=True, verbose_name='role')),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_last_modified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date last modified')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='x2', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members1', to='ihub.Organization')),
            ],
            options={
                'ordering': ['organization', 'person'],
            },
        ),
        migrations.CreateModel(
            name='RelationshipRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(unique=True, verbose_name='level')),
                ('name', models.CharField(max_length=255, verbose_name='description (English)')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='description (French)')),
            ],
            options={
                'ordering': ['level'],
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name (en)')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name (en)')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=25, null=True, verbose_name='title')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='last name')),
                ('phone_1', models.CharField(blank=True, max_length=100, null=True, verbose_name='work phone')),
                ('phone_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='work phone 2')),
                ('email_1', models.EmailField(blank=True, max_length=254, null=True, verbose_name='work email')),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='work email 2')),
                ('cell', models.CharField(blank=True, max_length=100, null=True, verbose_name='work phone (mobile)')),
                ('fax', models.CharField(blank=True, max_length=100, null=True, verbose_name='fax')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('email_block', models.TextField(blank=True, null=True, verbose_name='email block')),
                ('date_last_modified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date last modified')),
                ('old_id', models.IntegerField(blank=True, null=True)),
                ('ihub_vetted', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='vetted by iHub')),
                ('connected_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ihub_persons', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delete123', to='shared_models.Language', verbose_name='language preference')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='masterlist_person_last_modified_by_123', to=settings.AUTH_USER_MODEL, verbose_name='last modified by')),
                ('organizations', models.ManyToManyField(blank=True, related_name='org2', through='ihub.OrganizationMember', to='ihub.Organization', verbose_name='membership')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='ihub.Person'),
        ),
        migrations.AddField(
            model_name='organization',
            name='relationship_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='ihub.RelationshipRating', verbose_name='relationship rating'),
        ),
        migrations.AddField(
            model_name='organization',
            name='reserves',
            field=models.ManyToManyField(blank=True, to='ihub.Reserve', verbose_name='Associated reserves'),
        ),
        migrations.AddField(
            model_name='organization',
            name='sectors',
            field=models.ManyToManyField(blank=True, to='ihub.Sector', verbose_name='DFO sector'),
        ),
        migrations.AlterUniqueTogether(
            name='organizationmember',
            unique_together={('organization', 'person')},
        ),
    ]

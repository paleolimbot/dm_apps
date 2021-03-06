# Generated by Django 2.2.2 on 2020-04-29 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import travel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_models', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='trip title (English)')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='trip title (French)')),
                ('is_adm_approval_required', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='does attendance to this require ADM approval?')),
                ('location', models.CharField(max_length=1000, null=True, verbose_name='location (city, province, country)')),
                ('has_event_template', models.NullBooleanField(default=False, verbose_name='Is there an event template being completed for this conference or meeting?')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='event number')),
                ('start_date', models.DateTimeField(verbose_name='start date of event')),
                ('end_date', models.DateTimeField(verbose_name='end date of event')),
                ('meeting_url', models.URLField(blank=True, null=True, verbose_name='meeting URL')),
                ('abstract_deadline', models.DateTimeField(blank=True, null=True, verbose_name='abstract submission deadline')),
                ('registration_deadline', models.DateTimeField(blank=True, null=True, verbose_name='registration deadline')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='general notes')),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified?')),
                ('cost_warning_sent', models.DateTimeField(blank=True, null=True)),
                ('fiscal_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trips', to='shared_models.FiscalYear', verbose_name='fiscal year')),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='meeting_leads', to='shared_models.Region', verbose_name='Which region is the lead on this trip?')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trips_verified_by', to=settings.AUTH_USER_MODEL, verbose_name='verified by')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='CostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='HelpText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255)),
                ('eng_text', models.TextField(verbose_name='English text')),
                ('fra_text', models.TextField(blank=True, null=True, verbose_name='French text')),
            ],
            options={
                'ordering': ['field_name'],
            },
        ),
        migrations.CreateModel(
            name='NJCRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (eng)')),
                ('nom', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (fre)')),
                ('description_eng', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description (eng)')),
                ('description_fre', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description (fre)')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (eng)')),
                ('nom', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (fre)')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ReviewerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (eng)')),
                ('nom', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (fre)')),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (eng)')),
                ('nom', models.CharField(blank=True, max_length=100, null=True, verbose_name='name (fre)')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_for', models.IntegerField(choices=[(1, 'Reviewer status'), (2, 'Trip status')])),
                ('name', models.CharField(max_length=255)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'ordering': ['used_for', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TripRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public_servant', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Is the traveller a public servant?')),
                ('is_research_scientist', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Is the traveller a research scientist (RES)?')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='last name')),
                ('address', models.CharField(blank=True, max_length=1000, null=True, verbose_name='address')),
                ('phone', models.CharField(blank=True, max_length=1000, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='company name')),
                ('is_group_request', models.BooleanField(default=False, verbose_name='Is this a group request (i.e., a request for multiple individuals)?')),
                ('departure_location', models.CharField(blank=True, max_length=1000, null=True, verbose_name='departure location (city, province, country)')),
                ('destination', models.CharField(blank=True, max_length=1000, null=True, verbose_name='destination location (city, province, country)')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='start date of travel')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='end date of travel')),
                ('role_of_participant', models.TextField(blank=True, null=True, verbose_name='role description')),
                ('objective_of_event', models.TextField(blank=True, null=True, verbose_name='objective of the trip')),
                ('benefit_to_dfo', models.TextField(blank=True, null=True, verbose_name='benefit to DFO')),
                ('multiple_conferences_rationale', models.TextField(blank=True, null=True, verbose_name='rationale for individual attending multiple conferences')),
                ('multiple_attendee_rationale', models.TextField(blank=True, null=True, verbose_name='rationale for multiple travelers')),
                ('late_justification', models.TextField(blank=True, null=True, verbose_name='Justification for late submissions')),
                ('funding_source', models.TextField(blank=True, null=True, verbose_name='funding source')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='optional notes')),
                ('non_dfo_costs', models.FloatField(blank=True, null=True, verbose_name='Amount of non-DFO funding (CAD)')),
                ('non_dfo_org', models.CharField(blank=True, max_length=1000, null=True, verbose_name='full name(s) of organization providing non-DFO funding')),
                ('submitted', models.DateTimeField(blank=True, null=True, verbose_name='date submitted')),
                ('original_submission_date', models.DateTimeField(blank=True, null=True, verbose_name='original submission date')),
                ('admin_notes', models.TextField(blank=True, null=True, verbose_name='Administrative notes')),
                ('exclude_from_travel_plan', models.BooleanField(default=False, verbose_name='Exclude this traveller from the travel plan?')),
                ('bta_attendees', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Other attendees covered under BTA')),
                ('fiscal_year', models.ForeignKey(blank=True, default=2021, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='shared_models.FiscalYear', verbose_name='fiscal year')),
                ('parent_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_requests', to='travel.TripRequest')),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='travel.Purpose', verbose_name='purpose of travel')),
                ('reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='travel.Reason', verbose_name='reason for travel')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='shared_models.Region', verbose_name='Traveller belongs to which DFO region')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='travel.Role', verbose_name='role of traveller')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='shared_models.Section', verbose_name='under which DFO section is this request being made')),
                ('status', models.ForeignKey(default=8, limit_choices_to={'used_for': 2}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='travel.Status', verbose_name='trip status')),
                ('trip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_requests', to='travel.Conference', verbose_name='trip')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_trip_requests', to=settings.AUTH_USER_MODEL, verbose_name='DM Apps user')),
            ],
            options={
                'ordering': ['-start_date', 'last_name'],
                'unique_together': {('user', 'parent_request')},
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='caption')),
                ('file', models.FileField(null=True, upload_to=travel.models.file_directory_path, verbose_name='file attachment')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('trip_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='travel.TripRequest')),
            ],
            options={
                'ordering': ['trip_request', 'date_created'],
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('cost_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='costs', to='travel.CostCategory', verbose_name='category')),
            ],
            options={
                'ordering': ['cost_category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TripRequestCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_cad', models.FloatField(blank=True, null=True, verbose_name='daily rate (CAD/day)')),
                ('number_of_days', models.FloatField(blank=True, null=True, verbose_name='number of days')),
                ('amount_cad', models.FloatField(blank=True, default=0, null=True, verbose_name='amount (CAD)')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trip_request_costs', to='travel.Cost', verbose_name='cost')),
                ('trip_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_request_costs', to='travel.TripRequest', verbose_name='trip request')),
            ],
            options={
                'unique_together': {('trip_request', 'cost')},
            },
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(null=True, verbose_name='process order')),
                ('status_date', models.DateTimeField(blank=True, null=True, verbose_name='status date')),
                ('comments', models.TextField(null=True, verbose_name='Comments')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='travel.ReviewerRole', verbose_name='role')),
                ('status', models.ForeignKey(default=4, limit_choices_to={'used_for': 1}, on_delete=django.db.models.deletion.DO_NOTHING, to='travel.Status', verbose_name='review status')),
                ('trip_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewers', to='travel.TripRequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviewers', to=settings.AUTH_USER_MODEL, verbose_name='DM Apps user')),
            ],
            options={
                'ordering': ['trip_request', 'order'],
                'unique_together': {('trip_request', 'user', 'role')},
            },
        ),
    ]

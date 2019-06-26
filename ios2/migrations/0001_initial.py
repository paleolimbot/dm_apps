# Generated by Django 2.2.2 on 2019-06-18 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_type', models.CharField(choices=[('AMAR', 'AMAR'), ('Baker Traps', 'Baker Traps'), ('SBE uCat', 'SB uCat'), ('SBE ODO', 'SB ODO'), ('SBE IDO', 'SB IDO'), ('SBE16+', 'SBE16+'), ('SBE19+', 'SBE19+'), ('SBE37 NoPump', 'SBE37 NoPump'), ('SBE37 W/Pump', 'SBE37 W/Pump'), ('SBE SeaFET', 'SBE SeaFET'), ('SBE SeapHox', 'SBE SeapHox'), ('TRDI LR75kHz', 'TRDI LR75kHz'), ('ADCP 150kHz', 'ADCP 150kHz'), ('ADCP 300kHz', 'ADCP 300kHz'), ('ADCP 600kHz', 'ADCP 600kHz'), ('Nortek Aquadopps', 'Nortek Aquadopps'), ('SONTEK Argonaut', 'SONTEK Argonaut'), ('RBR Virtuoso', 'RBR Virtuoso'), ('Wildlife Acoustics SM2M+', 'Wildlife Acoustics SM2M+'), ('Wildlife Acoustics SM3M', 'Wildlife Acoustics SM3M'), ('Multi Electronique Aural M2', 'Multi Electronique Aural M2'), ('AR861 Acoustic Release', 'AR861 Acoustic Release'), ('CTD', 'CTD'), ('OXY', 'OXY')], default='SBE16+', max_length=20, verbose_name='Instrument Type')),
                ('serial_number', models.CharField(default='00000', max_length=20, verbose_name='Serial ID')),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase Date')),
                ('project_title', models.TextField(blank=True, null=True, verbose_name='Project title')),
                ('scientist', models.TextField(blank=True, null=True, verbose_name='Scientist')),
                ('connector', models.CharField(blank=True, choices=[('CIRCULAR', 'CIRCULAR'), ('RA', 'RA')], max_length=20, null=True, verbose_name='Connector Type')),
                ('comm_port', models.CharField(blank=True, choices=[('232', '232'), ('422', '422')], max_length=20, null=True, verbose_name='COMM Port')),
                ('location', models.CharField(default='HOME IOS', max_length=20, verbose_name='Location')),
                ('date_of_next_service', models.DateField(blank=True, null=True, verbose_name='Next Service Date')),
                ('is_sensor', models.BooleanField(default=False, verbose_name='Is Sensor?')),
                ('asset_tag', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Asset Tag')),
            ],
            options={
                'ordering': ['instrument_type', 'serial_number', 'purchase_date', 'project_title'],
                'unique_together': {('instrument_type', 'serial_number')},
            },
        ),
        migrations.CreateModel(
            name='InstrumentMooring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.TextField(blank=True)),
                ('orientation', models.TextField(blank=True, choices=[('UP', 'UP'), ('DOWN', 'DOWN')], null=True, verbose_name='Orientation')),
                ('instrument', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='instrudeploy', to='ios2.Instrument', verbose_name='instrument')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Calibration'), (2, 'Repair'), (3, 'Repair&Calib')], verbose_name='category')),
                ('service_date', models.DateField(blank=True, null=True, verbose_name='Service Date')),
                ('next_service_date', models.DateField(blank=True, null=True, verbose_name='Next Service Date')),
                ('comments', models.TextField(blank=True)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='ios2.Instrument', verbose_name='instrument')),
            ],
            options={
                'get_latest_by': ['service_date'],
            },
        ),
        migrations.CreateModel(
            name='Mooring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mooring', models.CharField(blank=True, max_length=200, null=True, verbose_name='mooring name')),
                ('mooring_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='mooring number')),
                ('deploy_time', models.DateTimeField(blank=True, null=True, verbose_name='deploy time (UTC)')),
                ('recover_time', models.DateTimeField(blank=True, null=True, verbose_name='recover time (UTC)')),
                ('lat', models.TextField(blank=True, null=True, verbose_name='lat')),
                ('lon', models.TextField(blank=True, null=True, verbose_name='lon')),
                ('depth', models.TextField(blank=True, null=True, verbose_name='depth')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='comments')),
                ('submitted', models.BooleanField(default=False, verbose_name='Submit moorings for review')),
                ('instruments', models.ManyToManyField(blank=True, related_name='moorings', through='ios2.InstrumentMooring', to='ios2.Instrument')),
            ],
            options={
                'ordering': ['mooring', 'mooring_number'],
                'unique_together': {('mooring', 'mooring_number')},
            },
        ),
        migrations.AddField(
            model_name='instrumentmooring',
            name='mooring',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='instrudeploy', to='ios2.Mooring', verbose_name='mooring'),
        ),
        migrations.AlterUniqueTogether(
            name='instrumentmooring',
            unique_together={('instrument', 'mooring')},
        ),
    ]
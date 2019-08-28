# Generated by Django 2.2.2 on 2019-07-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0020_auto_20190721_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='consultation_protocol',
            field=models.TextField(blank=True, null=True, verbose_name='consultation protocol (iHub only)'),
        ),
        migrations.AddField(
            model_name='organization',
            name='council_quorum',
            field=models.IntegerField(blank=True, null=True, verbose_name='council quorum (iHub only)'),
        ),
        migrations.AddField(
            model_name='organization',
            name='former_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Legal band name (iHub only)'),
        ),
        migrations.AddField(
            model_name='organization',
            name='legal_band_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Legal band name (iHub only)'),
        ),
        migrations.AddField(
            model_name='organization',
            name='mailing_address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='mailing address'),
        ),
        migrations.AddField(
            model_name='organization',
            name='processing_plant',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=False, verbose_name='processing plant on reserve? (iHub only)'),
        ),
        migrations.AddField(
            model_name='organization',
            name='wharf',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=False, verbose_name='Wharf on reserve? (iHub only)'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='street address'),
        ),
        migrations.AlterField(
            model_name='person',
            name='ihub_vetted',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=False, verbose_name='vetted by iHub'),
        ),
    ]
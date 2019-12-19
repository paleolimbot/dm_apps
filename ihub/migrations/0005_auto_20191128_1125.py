# Generated by Django 2.2.2 on 2019-11-28 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ihub', '0004_auto_20191127_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name (English)')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='name (French)')),
                ('abbrev_eng', models.CharField(blank=True, max_length=255, null=True, verbose_name='abbreviation (French)')),
                ('abbrev_fre', models.CharField(blank=True, max_length=255, null=True, verbose_name='abbreviation (French)')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='entry',
            name='funding_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='ihub.FundingProgram', verbose_name='funding program'),
        ),
    ]
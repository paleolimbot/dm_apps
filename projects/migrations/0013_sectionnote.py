# Generated by Django 2.2.2 on 2019-12-03 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared_models', '0025_region_head'),
        ('projects', '0012_project_meeting_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pressures', models.TextField(blank=True, null=True)),
                ('general_notes', models.TextField(blank=True, null=True)),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_notes', to='shared_models.FiscalYear')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='shared_models.Section')),
            ],
        ),
    ]

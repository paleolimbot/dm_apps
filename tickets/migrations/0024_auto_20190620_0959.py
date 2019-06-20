# Generated by Django 2.2.2 on 2019-06-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0023_auto_20190604_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='app',
            field=models.CharField(blank=True, choices=[('general', 'n/a'), ('camp', 'CAMP db'), ('diets', 'Marine diets'), ('esee', 'ESEE (not part of site)'), ('grais', 'grAIS'), ('herring', 'HerMorrhage'), ('ihub', 'iHub'), ('inventory', 'Metadata Inventory'), ('ios2', 'Instruments'), ('masterlist', 'Masterlist'), ('meq', 'Marine environmental quality (MEQ)'), ('oceanography', 'Oceanography'), ('plankton', 'Plankton Net (not part of site)'), ('projects', 'Science project planning'), ('publications', 'Project Publications Inventory'), ('scifi', 'SciFi'), ('shares', 'Gulf Shares'), ('snowcrab', 'Snowcrab'), ('spot', 'G&C App (Spot)'), ('staff', 'Staff Planning Tool'), ('tickets', 'Data Management Tickets'), ('travel', 'Travel Management System')], default='general', max_length=25, null=True, verbose_name='application name'),
        ),
    ]

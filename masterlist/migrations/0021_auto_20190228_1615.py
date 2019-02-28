# Generated by Django 2.1.4 on 2019-02-28 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0020_auto_20190228_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationinstruction',
            name='letter_cc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='include on cc (letter)'),
        ),
        migrations.AlterField(
            model_name='consultationinstruction',
            name='letter_to',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='address letter to:'),
        ),
        migrations.AlterField(
            model_name='consultationinstruction',
            name='paper_copy',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='paper copy to'),
        ),
        migrations.AlterField(
            model_name='consultationinstructionrecipient',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='consultation_instructions', to='masterlist.OrganizationMember'),
        ),
        migrations.AlterField(
            model_name='organizationmember',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='memberships', to='masterlist.Person'),
        ),
    ]

# Generated by Django 2.2.2 on 2020-07-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0002_consultationrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
        migrations.AlterField(
            model_name='nation',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='relationshiprating',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='relationshiprating',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='role',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name (en)'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name (fr)'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0024_auto_20190725_0916'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='organization',
            name='orgs',
            field=models.ManyToManyField(blank=True, to='masterlist.Organization', verbose_name='Associated organizations'),
        ),
        migrations.AddField(
            model_name='organization',
            name='reserves',
            field=models.ManyToManyField(blank=True, to='masterlist.Reserve', verbose_name='Associated reserves'),
        ),
    ]

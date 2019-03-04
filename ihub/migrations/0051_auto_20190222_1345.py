# Generated by Django 2.1.4 on 2019-02-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihub', '0050_auto_20190221_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationmember',
            name='roles',
            field=models.ManyToManyField(to='ihub.MemberRole'),
        ),
        migrations.AlterUniqueTogether(
            name='organizationmember',
            unique_together={('organization', 'person')},
        ),
    ]
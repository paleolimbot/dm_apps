# Generated by Django 2.2.2 on 2020-07-07 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whalebrary', '0005_auto_20200706_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='tag')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='lent_to',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='status',
        ),
        migrations.AddField(
            model_name='transaction',
            name='comments',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='comments'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_by',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='quantity')),
                ('date_ordered', models.DateTimeField(blank=True, help_text='Format: mm/dd/yyyy', null=True, verbose_name='date')),
                ('date_received', models.DateTimeField(blank=True, help_text='Format: mm/dd/yyyy', null=True, verbose_name='date')),
                ('confirm_received', models.BooleanField(default=False, verbose_name='order received')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='whalebrary.Item', verbose_name='item')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='whalebrary.Transaction', verbose_name='transaction')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='whalebrary.TransactionCategory', verbose_name='transaction category'),
            preserve_default=False,
        ),
    ]
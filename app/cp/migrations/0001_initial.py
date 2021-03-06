# Generated by Django 4.0.5 on 2022-07-06 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('num_order', models.CharField(max_length=255)),
                ('time_job', models.DecimalField(decimal_places=2, max_digits=3)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Number of order',
                'verbose_name_plural': 'Number of order',
                'db_table': 'content"."order',
            },
        ),
        migrations.CreateModel(
            name='Work_place',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('day_today', models.DateField()),
                ('psc', models.IntegerField()),
                ('job_time', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pre_time', models.PositiveIntegerField(default=0)),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cp.order')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Date of the job',
                'verbose_name_plural': 'Date of the job',
                'db_table': 'content"."work_place',
            },
        ),
    ]

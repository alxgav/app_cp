# Generated by Django 4.0.5 on 2022-09-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='num_order',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

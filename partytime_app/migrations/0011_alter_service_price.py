# Generated by Django 4.2.7 on 2023-11-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partytime_app', '0010_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(),
        ),
    ]

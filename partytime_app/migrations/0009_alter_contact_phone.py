# Generated by Django 4.2.7 on 2023-11-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partytime_app', '0008_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]

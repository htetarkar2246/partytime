# Generated by Django 4.2.7 on 2023-11-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partytime_app', '0009_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(max_length=999999)),
                ('service', models.CharField(max_length=100)),
            ],
        ),
    ]

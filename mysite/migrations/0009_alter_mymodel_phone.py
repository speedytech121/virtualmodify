# Generated by Django 3.2.21 on 2023-09-14 17:22

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_mymodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
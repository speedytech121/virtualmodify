# Generated by Django 3.2.21 on 2023-09-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20230914_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.2.21 on 2023-09-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_remove_mymodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='phone',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='message',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
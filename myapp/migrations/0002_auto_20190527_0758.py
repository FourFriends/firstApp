# Generated by Django 2.2.1 on 2019-05-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='bFinish',
            field=models.BooleanField(),
        ),
    ]

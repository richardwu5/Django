# Generated by Django 2.1 on 2018-09-10 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0027_auto_20180909_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialtypizza',
            name='size',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
# Generated by Django 2.1 on 2018-08-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0012_auto_20180830_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otheritem',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
# Generated by Django 2.1 on 2018-08-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0015_auto_20180830_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='type',
            field=models.CharField(choices=[('M', 'Meat'), ('V', 'Vegetables'), ('O', 'Others')], default='M', max_length=16),
        ),
    ]

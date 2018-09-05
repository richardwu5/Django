# Generated by Django 2.1 on 2018-08-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20180829_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='option',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('S', (('small', 'Small'), ('20', '20'))), ('M', (('medium', 'Medium'), ('25', '25'))), ('L', (('large', 'Large'), ('30', '30'))), ('XL', (('extra large', 'Extra Large'), ('35', '35')))], default='S', max_length=2),
        ),
    ]
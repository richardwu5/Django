# Generated by Django 2.1 on 2018-08-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20180829_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialtyPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]

# Generated by Django 2.1 on 2018-09-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0028_auto_20180909_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(max_length=100)),
                ('size', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='otherlist',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='pizzalist',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='spizzalist',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='cart', to='pizza.Item'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-03 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='NOP.png', upload_to='customers'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_mycart'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(blank=True, default='Pune', max_length=200),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='pincode',
            field=models.CharField(default=0, max_length=10),
        ),
    ]

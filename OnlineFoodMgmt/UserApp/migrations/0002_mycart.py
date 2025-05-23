# Generated by Django 4.2.3 on 2023-07-25 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]

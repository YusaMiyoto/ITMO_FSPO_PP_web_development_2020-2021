# Generated by Django 3.1.6 on 2021-03-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progect_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ManyToManyField(through='progect_first_app.Ownership', to='progect_first_app.Car_owner'),
        ),
    ]
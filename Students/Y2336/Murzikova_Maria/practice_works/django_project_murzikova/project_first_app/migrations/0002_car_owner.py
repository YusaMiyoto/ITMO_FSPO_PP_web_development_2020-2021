# Generated by Django 3.1.7 on 2021-03-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ManyToManyField(through='project_first_app.Hold', to='project_first_app.Owner'),
        ),
    ]
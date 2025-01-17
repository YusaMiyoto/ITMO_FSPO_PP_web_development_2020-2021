# Generated by Django 3.1.6 on 2021-03-23 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('mark', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('bDay', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenseNumber', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('issueDate', models.DateField()),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.owner')),
            ],
        ),
    ]

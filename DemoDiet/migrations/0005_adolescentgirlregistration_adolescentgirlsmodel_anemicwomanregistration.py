# Generated by Django 3.0.8 on 2021-01-29 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DemoDiet', '0004_auto_20210108_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdolescentGirlsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=2000)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(max_length=20)),
                ('bmi', models.IntegerField()),
                ('age', models.IntegerField()),
                ('hemoglobinvalue', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date', models.DateField()),
                ('recommendedfood', models.CharField(max_length=2000)),
                ('complication', models.CharField(max_length=2000)),
                ('education', models.CharField(max_length=2000)),
                ('medication', models.CharField(max_length=2000)),
                ('healthparameters', models.CharField(max_length=2000)),
                ('medicaladvice', models.CharField(max_length=2000)),
                ('uploaddocuments', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('deedback', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='AnemicWomanRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdolescentGirlRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

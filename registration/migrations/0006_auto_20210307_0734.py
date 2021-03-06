# Generated by Django 3.1.7 on 2021-03-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20210307_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='anganwadiworker',
            name='ICDScenteraddress',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='ICDScontact',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='ICDSname',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='age',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='contact',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='dob',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='education',
            field=models.CharField(blank=True, choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=2000),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='monthlyincome',
            field=models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=1000),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='occupation',
            field=models.CharField(blank=True, choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2000),
        ),
        migrations.AddField(
            model_name='anganwadiworker',
            name='profilephoto',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]

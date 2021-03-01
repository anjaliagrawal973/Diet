# Generated by Django 3.1.1 on 2021-02-27 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DemoDiet', '0007_smmotherregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adolescentgirlregistration',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdolescentGirlsModel',
        ),
        migrations.RemoveField(
            model_name='anemicwomanregistration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='anganwadiworker',
            name='user',
        ),
        migrations.DeleteModel(
            name='BodyModel',
        ),
        migrations.DeleteModel(
            name='bulk_reg',
        ),
        migrations.DeleteModel(
            name='DailyScheduleForm',
        ),
        migrations.DeleteModel(
            name='DietModel',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='EatTodayModel',
        ),
        migrations.DeleteModel(
            name='FeedbackModel',
        ),
        migrations.RemoveField(
            model_name='headmentor',
            name='user',
        ),
        migrations.DeleteModel(
            name='image_up',
        ),
        migrations.RemoveField(
            model_name='mukhyasevika',
            name='user',
        ),
        migrations.DeleteModel(
            name='PersonalInformationForms',
        ),
        migrations.RemoveField(
            model_name='pregnantwomanregistration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projectcoordinator',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projectmanager',
            name='user',
        ),
        migrations.RemoveField(
            model_name='school',
            name='user',
        ),
        migrations.RemoveField(
            model_name='schoolcoordinator',
            name='user',
        ),
        migrations.RemoveField(
            model_name='smmotherregistration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='supportmentor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='technicalexpert',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdolescentGirlRegistration',
        ),
        migrations.DeleteModel(
            name='AnemicWomanRegistration',
        ),
        migrations.DeleteModel(
            name='AnganwadiWorker',
        ),
        migrations.DeleteModel(
            name='HeadMentor',
        ),
        migrations.DeleteModel(
            name='MukhyaSevika',
        ),
        migrations.DeleteModel(
            name='PregnantWomanRegistration',
        ),
        migrations.DeleteModel(
            name='ProjectCoordinator',
        ),
        migrations.DeleteModel(
            name='ProjectManager',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='SchoolCoordinator',
        ),
        migrations.DeleteModel(
            name='SMMotherRegistration',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='SupportMentor',
        ),
        migrations.DeleteModel(
            name='TechnicalExpert',
        ),
    ]
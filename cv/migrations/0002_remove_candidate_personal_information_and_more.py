# Generated by Django 5.1.1 on 2024-11-20 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='personal_information',
        ),
        migrations.RenameField(
            model_name='additionalinformation',
            old_name='candidate',
            new_name='Candidate',
        ),
        migrations.RenameField(
            model_name='workexperience',
            old_name='candidate',
            new_name='Candidate',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='additional_information',
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='cv.candidate')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

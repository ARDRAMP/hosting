# Generated by Django 3.2.7 on 2024-02-18 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educonnect', '0003_rename_fid_study_materials_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=150)),
                ('m_id', models.CharField(max_length=150)),
                ('s_msg', models.CharField(max_length=150)),
                ('m_msg', models.CharField(max_length=150)),
            ],
        ),
    ]
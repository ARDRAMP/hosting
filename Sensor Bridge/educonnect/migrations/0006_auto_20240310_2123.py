# Generated by Django 3.2.7 on 2024-03-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educonnect', '0005_rename_card_name_course_payment_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_payment',
            name='order_id',
        ),
        migrations.AddField(
            model_name='study_materials',
            name='c_id',
            field=models.CharField(default=-2013, max_length=150),
            preserve_default=False,
        ),
    ]
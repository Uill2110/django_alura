# Generated by Django 5.1 on 2024-09-21 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0013_alter_course_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]

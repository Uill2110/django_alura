# Generated by Django 5.1 on 2024-09-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0010_alter_course_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]

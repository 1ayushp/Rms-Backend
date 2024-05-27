# Generated by Django 4.2.4 on 2023-12-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_course_department_remove_course_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='section',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='room_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='routine',
            name='teacher',
            field=models.ManyToManyField(blank=True, null=True, to='api.teacher'),
        ),
    ]

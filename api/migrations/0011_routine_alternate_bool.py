# Generated by Django 4.1.13 on 2024-04-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_routine_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='alternate_bool',
            field=models.BooleanField(default=False),
        ),
    ]

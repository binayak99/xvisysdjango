# Generated by Django 3.2.7 on 2021-11-13 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_remove_volunteerarea_familyid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerevent',
            name='volunteerarea',
        ),
    ]

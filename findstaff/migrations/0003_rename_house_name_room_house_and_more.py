# Generated by Django 5.0.6 on 2024-06-05 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findstaff', '0002_alter_room_house_name_alter_staff_staff_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='house_name',
            new_name='house',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_room_name',
            new_name='room',
        ),
    ]

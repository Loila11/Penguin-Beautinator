# Generated by Django 3.0.2 on 2020-06-13 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautinator', '0006_auto_20200613_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salon',
            old_name='phone',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='phone_no',
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-18 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperatura', '0010_auto_20190918_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='custom_city',
            new_name='custom_name_city',
        ),
    ]

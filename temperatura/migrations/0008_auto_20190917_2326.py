# Generated by Django 2.2.5 on 2019-09-17 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperatura', '0007_auto_20190917_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cidade',
            old_name='nome',
            new_name='city',
        ),
    ]

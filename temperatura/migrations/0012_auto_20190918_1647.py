# Generated by Django 2.2.5 on 2019-09-18 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temperatura', '0011_auto_20190918_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temps', to='temperatura.City'),
        ),
    ]

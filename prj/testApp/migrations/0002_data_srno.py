# Generated by Django 5.2.4 on 2025-07-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='srNo',
            field=models.IntegerField(default=0),
        ),
    ]

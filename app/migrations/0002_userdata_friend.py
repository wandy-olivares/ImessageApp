# Generated by Django 4.1.7 on 2023-04-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='friend',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
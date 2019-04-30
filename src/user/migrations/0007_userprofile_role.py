# Generated by Django 2.2 on 2019-04-27 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('EM', 'Employee'), ('HR', 'Manager')], default='EM', max_length=2),
        ),
    ]
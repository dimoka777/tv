# Generated by Django 2.2.3 on 2019-07-10 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0004_auto_20190710_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tv_choice',
        ),
    ]

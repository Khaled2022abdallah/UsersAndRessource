# Generated by Django 4.1.3 on 2022-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

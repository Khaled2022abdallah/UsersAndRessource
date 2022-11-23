# Generated by Django 4.1.3 on 2022-11-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1000)),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('avatar', models.URLField()),
                ('job', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('urlSupport', models.URLField()),
                ('textSupport', models.TextField()),
            ],
        ),
    ]

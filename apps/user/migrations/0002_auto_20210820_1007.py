# Generated by Django 3.2.6 on 2021-08-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='country_of_news',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='news_source',
            field=models.TextField(blank=True, null=True),
        ),
    ]

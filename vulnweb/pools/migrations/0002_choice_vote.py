# Generated by Django 5.1.4 on 2024-12-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
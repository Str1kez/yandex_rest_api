# Generated by Django 4.0.2 on 2022-06-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopunit',
            name='date',
            field=models.DateTimeField(default='2022-05-28T21:12:01.000Z'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.10 on 2020-09-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='mark_id',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_models_mark_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='mark_id',
            field=models.IntegerField(null=True),
        ),
    ]
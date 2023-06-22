# Generated by Django 4.2.2 on 2023-06-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_alter_models_mark_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarksModels',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(max_length=255, verbose_name='Mark name')),
                ('model', models.CharField(max_length=255, verbose_name='Model name')),
            ],
        ),
        migrations.DeleteModel(
            name='Models',
        ),
    ]

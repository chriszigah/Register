# Generated by Django 4.2.11 on 2024-05-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_alter_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(default='15ec37dd1fc64cde8991004d237fb0f7', primary_key=True, serialize=False),
        ),
    ]

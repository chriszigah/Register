# Generated by Django 4.2.11 on 2024-05-03 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_alter_record_record_id_alter_record_unique_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='record',
            name='record_id',
            field=models.CharField(default='REG959114', max_length=9, primary_key=True, serialize=False),
        ),
    ]

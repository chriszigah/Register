# Generated by Django 4.2.11 on 2024-05-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_alter_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(default='45d290bdd01c4bfca8616364646c423d', max_length=100, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.2.11 on 2024-05-03 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_alter_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.CharField(default='de88ad436af44d3eb231e53829583893', max_length=36, primary_key=True, serialize=False),
        ),
    ]

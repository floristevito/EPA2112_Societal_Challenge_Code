# Generated by Django 3.2.7 on 2021-11-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_feedback_safety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='qr_id',
            field=models.CharField(default='0_unknown', max_length=100),
        ),
    ]

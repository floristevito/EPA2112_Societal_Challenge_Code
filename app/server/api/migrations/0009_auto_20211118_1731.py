# Generated by Django 3.2.7 on 2021-11-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_feedback_qr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='frequency',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='qr_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='reasonOfVisit',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='safety',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='stars',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
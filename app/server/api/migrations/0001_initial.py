# Generated by Django 3.2.7 on 2021-10-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('long', models.FloatField()),
                ('feedback', models.CharField(max_length=1000)),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2021-02-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='name',
            field=models.CharField(default='Timothys', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fitnessrecord',
            name='calories',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='fitnessrecord',
            name='duration',
            field=models.DurationField(default='00:30:00', help_text='HH:MM:ss format'),
        ),
    ]

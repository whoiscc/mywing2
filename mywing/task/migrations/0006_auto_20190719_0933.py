# Generated by Django 2.2.1 on 2019-07-19 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20190719_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='accepted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='canceled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

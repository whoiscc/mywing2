# Generated by Django 2.2.1 on 2019-07-19 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20190719_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

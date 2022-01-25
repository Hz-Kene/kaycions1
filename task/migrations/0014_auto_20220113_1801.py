# Generated by Django 3.2.8 on 2022-01-13 17:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_auto_20220113_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='amount_withdraw',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_expiry_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 13, 17, 1, 29, 588832, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_expiry_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 13, 17, 1, 29, 588832, tzinfo=utc), null=True),
        ),
    ]

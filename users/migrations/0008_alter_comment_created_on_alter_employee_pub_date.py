# Generated by Django 4.2.7 on 2023-11-11 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_comment_created_on_alter_employee_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 11, 0, 49, 8, 915164, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 11, 0, 49, 8, 915164, tzinfo=datetime.timezone.utc)),
        ),
    ]

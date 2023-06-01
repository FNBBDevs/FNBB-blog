# Generated by Django 4.2.1 on 2023-06-01 01:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0026_alter_comment_date_alter_friend_since_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user_to_notify',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='notification_user_to_notify', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 20, 12, 0, 249703)),
        ),
        migrations.AlterField(
            model_name='friend',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 20, 12, 0, 249703)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 20, 12, 0, 250703)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 20, 12, 0, 249703)),
        ),
    ]

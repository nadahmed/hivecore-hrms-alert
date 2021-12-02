# Generated by Django 3.2.9 on 2021-12-01 08:06

import api.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LEAVE_APPROVAL', 'Leave Approval'), ('LEAVE_CREATED', 'Leave Created'), ('LEAVE_REJECTED', 'Leave Rjected'), ('LEAVE_NEW', 'Leave New'), ('LEAVE_PENDING', 'Leave Pending')], max_length=500)),
                ('created', models.DateTimeField(default=api.models.get_local_time, editable=False)),
                ('is_read', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

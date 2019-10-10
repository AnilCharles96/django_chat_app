# Generated by Django 2.2.4 on 2019-10-09 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_register_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.AlterField(
            model_name='register',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

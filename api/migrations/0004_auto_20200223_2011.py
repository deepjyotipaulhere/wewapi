# Generated by Django 2.2.6 on 2020-02-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200223_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='by',
        ),
        migrations.AddField(
            model_name='blog',
            name='by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Users'),
            preserve_default=False,
        ),
    ]

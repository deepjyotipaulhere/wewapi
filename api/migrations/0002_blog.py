# Generated by Django 2.2.6 on 2020-02-21 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Users')),
            ],
        ),
    ]

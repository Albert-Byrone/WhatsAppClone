# Generated by Django 3.1.2 on 2020-10-12 11:51

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('description', models.TextField(blank=True, help_text='description of the group')),
                ('mute_notifications', models.BooleanField(default=False, help_text='disable notification if true')),
                ('icon', models.ImageField(blank=True, help_text='Group icon', upload_to='chartgroup')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]

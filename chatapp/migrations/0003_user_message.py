# Generated by Django 5.1.4 on 2024-12-21 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_remove_group_id_alter_group_groupid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('usergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messagecontent', models.TextField()),
                ('messagegroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.group')),
                ('messagesender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.user')),
            ],
        ),
    ]

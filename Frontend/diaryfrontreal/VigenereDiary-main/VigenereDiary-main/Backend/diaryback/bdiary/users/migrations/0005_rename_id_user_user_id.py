# Generated by Django 4.2.15 on 2024-10-07 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_groups_user_is_superuser_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
    ]

# Generated by Django 4.2.15 on 2024-10-08 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_blacklistedaccesstoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklistedaccesstoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]

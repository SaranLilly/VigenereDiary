# Generated by Django 4.2.15 on 2024-10-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userspro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]

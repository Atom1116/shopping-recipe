# Generated by Django 3.0.6 on 2021-10-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='user_name'),
        ),
    ]

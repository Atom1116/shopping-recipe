# Generated by Django 3.0.6 on 2021-10-19 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211018_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(db_column='category_id', primary_key=True, serialize=False, verbose_name='category_id')),
                ('order', models.IntegerField(db_column='order', default=9999)),
                ('name', models.CharField(blank=True, db_column='name', default='', max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('uer_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

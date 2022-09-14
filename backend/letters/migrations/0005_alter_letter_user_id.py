# Generated by Django 4.0.7 on 2022-09-14 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letters', '0004_alter_anniversary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='user_id',
            field=models.ForeignKey(blank=True, db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

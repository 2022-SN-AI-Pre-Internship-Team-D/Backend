# Generated by Django 4.0.7 on 2022-09-11 17:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anniversary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date', models.DateTimeField()),
                ('is_active', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'anniversary',
            },
        ),
        migrations.CreateModel(
            name='letter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('text', models.CharField(max_length=255, unique=True)),
                ('file', models.CharField(max_length=255, unique=True)),
                ('is_active', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('anni_id', models.ForeignKey(db_column='anni_id', on_delete=django.db.models.deletion.CASCADE, to='letters.anniversary')),
            ],
            options={
                'db_table': 'letter',
            },
        ),
    ]

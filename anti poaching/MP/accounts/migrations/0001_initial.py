# Generated by Django 5.1.5 on 2025-02-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('position', models.CharField(choices=[('admin', 'Admin'), ('patrol', 'Patrol')], default='patrol', max_length=6)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]

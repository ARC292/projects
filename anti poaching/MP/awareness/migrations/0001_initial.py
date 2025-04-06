# Generated by Django 5.1.5 on 2025-03-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwarenessCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='carousel_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='carousel_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='carousel_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='carousel_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

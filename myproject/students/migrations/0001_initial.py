# Generated by Django 3.1.14 on 2025-03-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=10, unique=True)),
                ('course', models.CharField(blank=True, max_length=200, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('content', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

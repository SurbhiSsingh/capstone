# Generated by Django 3.1.14 on 2025-06-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('topic', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(choices=[('journal', 'Journal'), ('conference', 'Conference'), ('patent', 'Patent'), ('other', 'Other')], max_length=20)),
                ('link', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

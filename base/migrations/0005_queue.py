# Generated by Django 4.0.4 on 2022-11-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]

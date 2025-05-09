# Generated by Django 5.1.5 on 2025-04-21 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold')], max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('employee', models.ManyToManyField(to='api.employee')),
            ],
        ),
    ]

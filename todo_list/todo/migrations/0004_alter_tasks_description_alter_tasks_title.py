# Generated by Django 5.0.4 on 2024-05-31 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_tasks_options_tasks_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

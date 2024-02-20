# Generated by Django 5.0.1 on 2024-02-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roleplay_manager', '0015_remove_modelinfo_prompt_template_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_developer',
        ),
        migrations.AddField(
            model_name='modelinfo',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
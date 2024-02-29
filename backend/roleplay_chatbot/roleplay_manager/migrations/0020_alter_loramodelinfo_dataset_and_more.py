# Generated by Django 5.0.1 on 2024-02-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roleplay_manager', '0019_alter_loramodelinfo_lora_bias_loratrainingstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loramodelinfo',
            name='dataset',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loratrainingstatus',
            name='current_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('completed', 'Completed'), ('error', 'Error')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='loratrainingstatus',
            name='lora_training_error',
            field=models.TextField(default=''),
        ),
    ]
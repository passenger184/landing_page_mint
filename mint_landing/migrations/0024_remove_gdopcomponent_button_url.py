# Generated by Django 5.1.4 on 2025-01-09 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mint_landing', '0023_gdopcomponent_description_gdopcomponent_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gdopcomponent',
            name='button_url',
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mint_landing', '0010_rename_contactus_resource_remove_project_created_by_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gdopcomponent',
            options={'verbose_name': 'GDOP Component', 'verbose_name_plural': 'GDOP Components'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={},
        ),
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, help_text='Image for the announcement', null=True, upload_to='announcements/'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='slug',
            field=models.SlugField(blank=True, help_text='Slug for the announcement', max_length=120, unique=True),
        ),
    ]

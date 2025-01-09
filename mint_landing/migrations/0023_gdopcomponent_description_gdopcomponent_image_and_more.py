# Generated by Django 5.1.4 on 2025-01-09 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mint_landing', '0022_focusarea_created_by_focusarea_updated_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gdopcomponent',
            name='description',
            field=models.TextField(default='', help_text='Description of the component'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gdopcomponent',
            name='image',
            field=models.ImageField(blank=True, help_text='Image for the component', null=True, upload_to='uploads/components/'),
        ),
        migrations.AddField(
            model_name='gdopcomponent',
            name='key_advantages',
            field=models.CharField(default='', help_text='Comma separated list of advantages', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gdopcomponent',
            name='subtitle',
            field=models.CharField(help_text='A very short description', max_length=100),
        ),
    ]
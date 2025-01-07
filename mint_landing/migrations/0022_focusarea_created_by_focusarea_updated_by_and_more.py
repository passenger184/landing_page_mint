# Generated by Django 5.1.4 on 2025-01-07 22:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mint_landing', '0021_focusarea_footercontent_sociallink_usefullink'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='focusarea',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='focus_area_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='focus_area_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='footercontent',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footer_content_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='footercontent',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footer_content_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usefullink',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='useful_link_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usefullink',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='useful_link_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='footercontent',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/footer/'),
        ),
    ]
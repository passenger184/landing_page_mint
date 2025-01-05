# Generated by Django 5.1.4 on 2025-01-03 06:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mint_landing', '0009_aboutus_created_by_aboutus_updated_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='Resource',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated_by',
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title for the figure (e.g., Users, Projects)', max_length=100)),
                ('value', models.PositiveIntegerField(help_text='Value of the statistic')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='figure_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='figure_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Figures',
                'verbose_name_plural': 'Figures',
            },
        ),
        migrations.CreateModel(
            name='GDOPComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the component', max_length=100)),
                ('subtitle', models.TextField(help_text='Description of the component')),
                ('is_active', models.BooleanField(default=False)),
                ('icon_name', models.CharField(help_text='Bootstrap icon class name (e.g., bi-people', max_length=100)),
                ('button_url', models.URLField(blank=True, help_text='URL the button points to', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='component_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='component_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='NumberStatistic',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]

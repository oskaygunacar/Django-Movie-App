# Generated by Django 5.0.1 on 2024-01-10 13:38

import autoslug.fields
import slugify
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='get_username', slugify=slugify.slugify, unique=True),
        ),
    ]

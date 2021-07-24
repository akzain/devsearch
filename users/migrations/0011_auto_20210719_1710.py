# Generated by Django 3.0.3 on 2021-07-19 14:10

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210718_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_github',
            field=models.URLField(blank=True, null=True, validators=[users.models.validate_url_github]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_linkedin',
            field=models.URLField(blank=True, null=True, validators=[users.models.validate_url_linkedin]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_twitter',
            field=models.URLField(blank=True, null=True, validators=[users.models.validate_url_twitter]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_youtube',
            field=models.URLField(blank=True, null=True, validators=[users.models.validate_url_yt]),
        ),
    ]
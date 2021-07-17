# Generated by Django 3.0.3 on 2021-07-17 06:18

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210715_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_twitter',
            field=models.URLField(blank=True, null=True, validators=[users.models.validate_url_twitter]),
        ),
    ]

# Generated by Django 3.2.8 on 2022-01-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0021_auto_20220114_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='whatsapp_link',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]

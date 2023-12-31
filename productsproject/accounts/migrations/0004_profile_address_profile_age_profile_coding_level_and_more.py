# Generated by Django 4.2.7 on 2023-12-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='coding_level',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='iq_level',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]

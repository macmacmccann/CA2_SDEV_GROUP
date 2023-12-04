# Generated by Django 4.2.6 on 2023-12-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_address_remove_profile_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
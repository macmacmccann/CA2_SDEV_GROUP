# Generated by Django 4.2.7 on 2023-12-02 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_percentage_pass_rate'),
        ('accounts', '0004_profile_address_profile_age_profile_coding_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='coding_level',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='iq_level',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users'),
        ),
        migrations.AddField(
            model_name='profile',
            name='available_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fav_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='users'),
        ),
    ]
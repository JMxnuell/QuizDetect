# Generated by Django 4.1.4 on 2023-01-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0002_alter_post_user_likes_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../static/img/new_user.png', upload_to='images/'),
        ),
    ]
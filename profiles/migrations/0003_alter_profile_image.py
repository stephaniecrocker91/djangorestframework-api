# Generated by Django 3.2.15 on 2022-10-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../avatar_profile_mkm0cf', upload_to='images/'),
        ),
    ]

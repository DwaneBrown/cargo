# Generated by Django 3.0 on 2019-12-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bird', '0005_auto_20191212_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pics',
            name='cover',
        ),
        migrations.AddField(
            model_name='pics',
            name='image_cover',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]

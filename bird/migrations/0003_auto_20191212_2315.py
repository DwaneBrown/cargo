# Generated by Django 3.0 on 2019-12-12 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bird', '0002_auto_20191212_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(default='default.jpg', upload_to='images/')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.Editor')),
                ('tags', models.ManyToManyField(to='bird.tags')),
            ],
        ),
    ]
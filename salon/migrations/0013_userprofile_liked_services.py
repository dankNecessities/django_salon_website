# Generated by Django 2.0.1 on 2018-01-17 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0012_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked_services',
            field=models.ManyToManyField(to='salon.Service', verbose_name='list of liked services'),
        ),
    ]

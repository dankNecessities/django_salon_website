# Generated by Django 2.0.1 on 2018-01-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_auto_20180116_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='root',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]

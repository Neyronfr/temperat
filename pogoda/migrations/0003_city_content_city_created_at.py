# Generated by Django 5.0.4 on 2024-04-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pogoda', '0002_alter_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]

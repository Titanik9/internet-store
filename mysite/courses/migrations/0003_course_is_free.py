# Generated by Django 4.0 on 2022-07-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='Free?'),
        ),
    ]

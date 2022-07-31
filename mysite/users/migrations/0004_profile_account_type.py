# Generated by Django 4.0 on 2022-07-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Full options'), ('free', 'Free options')], default='free', max_length=30),
        ),
    ]
# Generated by Django 5.0 on 2024-04-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_alter_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Prefer not to say', 'Prefer not to say'), ('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]

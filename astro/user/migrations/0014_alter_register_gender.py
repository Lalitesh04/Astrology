# Generated by Django 5.0 on 2024-02-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Prefer not to say', 'Prefer not to say'), ('Female', 'Female'), ('Male', 'Male')], max_length=100),
        ),
    ]

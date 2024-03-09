# Generated by Django 5.0 on 2024-02-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_register_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='contact',
            field=models.CharField(default='123456', max_length=30),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='customer_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Prefer not to say', 'Prefer not to say'), ('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]

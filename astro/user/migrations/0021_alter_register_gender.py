# Generated by Django 5.0 on 2024-04-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_feedback_contact_alter_feedback_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Prefer not to say', 'Prefer not to say'), ('Female', 'Female')], max_length=100),
        ),
    ]
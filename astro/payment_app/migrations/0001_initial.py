# Generated by Django 5.0 on 2024-02-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'payment_table',
            },
        ),
    ]

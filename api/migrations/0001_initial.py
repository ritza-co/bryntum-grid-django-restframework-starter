# Generated by Django 5.0.2 on 2024-02-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('percentage_wins', models.IntegerField(default=0)),
            ],
        ),
    ]
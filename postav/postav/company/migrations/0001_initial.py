# Generated by Django 3.2.4 on 2021-06-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('pub', 'Public'), ('pri', 'Private')], max_length=3)),
                ('longitude', models.CharField(max_length=40)),
                ('latitude', models.CharField(max_length=40)),
                ('instagram', models.URLField(verbose_name='instagram')),
                ('facebook', models.URLField(verbose_name='facebook')),
                ('whatsapp', models.URLField(verbose_name='whatsapp')),
            ],
        ),
    ]

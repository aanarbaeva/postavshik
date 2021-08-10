# Generated by Django 3.2.5 on 2021-07-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(null=True, to='product.Category'),
        ),
    ]
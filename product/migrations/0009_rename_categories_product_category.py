# Generated by Django 3.2.5 on 2021-07-28 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_category_product_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-28 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='title',
        ),
    ]
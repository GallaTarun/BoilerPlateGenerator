# Generated by Django 3.2 on 2022-05-25 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGenerator', '0003_framework'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FilesAdmin',
            new_name='Project',
        ),
        migrations.DeleteModel(
            name='Framework',
        ),
    ]
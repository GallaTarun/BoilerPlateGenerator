# Generated by Django 3.2 on 2022-05-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGenerator', '0002_auto_20220525_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('frameworkId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('frameworkType', models.CharField(choices=[('', 'Select'), ('0', 'Frontend'), ('1', 'Backend')], max_length=30)),
                ('frameworkName', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0004_addesignation'),
    ]

    operations = [
        migrations.CreateModel(
            name='adcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]
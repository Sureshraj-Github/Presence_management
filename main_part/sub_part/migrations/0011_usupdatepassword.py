# Generated by Django 3.2.3 on 2021-06-13 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0010_usupdateinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='usupdatepassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldpassword', models.CharField(max_length=100)),
                ('newpassword', models.CharField(max_length=100)),
                ('retypepassword', models.CharField(max_length=100)),
            ],
        ),
    ]

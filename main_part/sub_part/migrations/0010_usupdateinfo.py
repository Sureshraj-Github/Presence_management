# Generated by Django 3.2.3 on 2021-06-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_adupdatepassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='usupdateinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

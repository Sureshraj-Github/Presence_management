# Generated by Django 3.2.3 on 2021-06-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0012_indexform'),
    ]

    operations = [
        migrations.CreateModel(
            name='adholiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdate', models.CharField(max_length=100)),
            ],
        ),
    ]

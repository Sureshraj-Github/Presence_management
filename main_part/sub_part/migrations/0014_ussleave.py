# Generated by Django 3.2.3 on 2021-06-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0013_adholiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='ussleave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavedate', models.CharField(max_length=100)),
                ('leavecategory', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]

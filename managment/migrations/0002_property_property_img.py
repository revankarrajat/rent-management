# Generated by Django 2.1.4 on 2018-12-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_img',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]

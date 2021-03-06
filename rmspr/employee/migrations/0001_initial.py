# Generated by Django 2.1.4 on 2018-12-19 11:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

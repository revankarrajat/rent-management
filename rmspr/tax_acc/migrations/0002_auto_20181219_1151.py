# Generated by Django 2.1.4 on 2018-12-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax_acc',
            name='tax_amt',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

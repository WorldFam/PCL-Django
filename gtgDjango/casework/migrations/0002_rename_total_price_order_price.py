# Generated by Django 4.0.4 on 2022-04-30 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casework', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='price',
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-06 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('romaapp', '0014_portfolio_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='updated',
        ),
    ]

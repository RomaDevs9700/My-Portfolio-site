# Generated by Django 4.0.3 on 2022-04-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romaapp', '0005_alter_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.SmallIntegerField(max_length=20, null=True),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='formregistration',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='reviews',
        ),
        migrations.DeleteModel(
            name='userimage',
        ),
    ]
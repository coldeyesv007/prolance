# Generated by Django 4.0.3 on 2022-04-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgget', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=10000)),
                ('time', models.TimeField(auto_now_add=True)),
                ('sender', models.CharField(max_length=10000000000)),
                ('receiver', models.CharField(max_length=10000000000)),
                ('mimg', models.ImageField(upload_to='')),
                ('mfname', models.CharField(max_length=30)),
                ('mlname', models.CharField(max_length=30)),
                ('msgpost', models.CharField(max_length=30)),
            ],
        ),
    ]
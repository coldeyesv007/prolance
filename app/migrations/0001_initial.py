# Generated by Django 4.0.3 on 2022-04-05 16:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('sjobtype', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
                ('fjob', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='formregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('job', models.CharField(max_length=20)),
                ('jobtype', models.CharField(max_length=20)),
                ('wage', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=60)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userget', models.CharField(max_length=20)),
                ('ruser', models.CharField(max_length=20, verbose_name=django.contrib.auth.models.User)),
                ('subject', models.CharField(max_length=20)),
                ('review', models.TextField(blank=True, max_length=100)),
                ('rating', models.FloatField()),
                ('rfname', models.CharField(max_length=20)),
                ('rlname', models.CharField(max_length=20)),
                ('rimg', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='userimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default/avatar.jpeg', upload_to='default')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

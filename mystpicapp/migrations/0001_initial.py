# Generated by Django 5.0.4 on 2024-05-05 16:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='images/category/')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryMystery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystpicapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Mystery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='images/mystery/')),
                ('description', models.TextField(max_length=1000)),
                ('answer', models.CharField(max_length=80)),
                ('date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(through='mystpicapp.CategoryMystery', to='mystpicapp.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=160)),
                ('date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mystery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystpicapp.mystery')),
            ],
        ),
        migrations.AddField(
            model_name='categorymystery',
            name='mystery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystpicapp.mystery'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

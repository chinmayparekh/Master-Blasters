# Generated by Django 4.0.2 on 2022-02-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pcell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_name', models.CharField(max_length=100)),
                ('College_website', models.URLField()),
                ('College_linkedin', models.URLField()),
                ('College_email', models.EmailField(max_length=254)),
                ('College_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=100)),
                ('Company_website', models.URLField()),
                ('Company_linkedin', models.URLField()),
                ('Company_email', models.EmailField(max_length=254)),
            ],
        ),
    ]

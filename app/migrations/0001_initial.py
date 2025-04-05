# Generated by Django 5.0.7 on 2025-04-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Title', models.CharField(max_length=100)),
                ('Author_name', models.CharField(max_length=100)),
                ('ISBN_Number', models.CharField(max_length=100)),
                ('Book_Description', models.TextField()),
                ('Genre', models.CharField(max_length=100)),
                ('Publisher', models.CharField(max_length=100)),
                ('Publication_Year', models.CharField(max_length=10)),
                ('copies_available', models.IntegerField()),
                ('rack_number', models.CharField(max_length=100)),
                ('Book_Url', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='images/')),
                ('Book_PDF', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]

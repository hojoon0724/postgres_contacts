# Generated by Django 5.0.3 on 2024-03-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=30)),
                ('phone2', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=254)),
                ('address2', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('state_province', models.CharField(max_length=254)),
                ('zip_postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=254)),
            ],
        ),
    ]
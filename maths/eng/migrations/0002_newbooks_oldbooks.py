# Generated by Django 3.2.5 on 2021-07-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('Edition', models.CharField(max_length=50)),
                ('Publication', models.CharField(max_length=50)),
                ('checkbox', models.CharField(max_length=50)),
                ('submit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oldbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('Edition', models.CharField(max_length=50)),
                ('Publication', models.CharField(max_length=50)),
            ],
        ),
    ]
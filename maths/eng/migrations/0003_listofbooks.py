# Generated by Django 3.2.5 on 2021-07-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0002_newbooks_oldbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='listofbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newbooks', models.IntegerField()),
                ('oldbooks', models.IntegerField()),
                ('totalbooks', models.IntegerField()),
            ],
        ),
    ]

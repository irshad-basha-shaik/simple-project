# Generated by Django 3.2.5 on 2021-07-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0008_nb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=50)),
                ('publication', models.CharField(max_length=50)),
            ],
        ),
    ]

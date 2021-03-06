# Generated by Django 3.2.4 on 2021-09-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='static/profile_img')),
                ('story', models.FileField(upload_to='static/story')),
            ],
        ),
    ]

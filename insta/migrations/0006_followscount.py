# Generated by Django 3.2.8 on 2021-10-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20211017_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowsCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=1000)),
            ],
        ),
    ]

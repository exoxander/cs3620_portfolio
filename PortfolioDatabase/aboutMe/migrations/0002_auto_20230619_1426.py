# Generated by Django 2.2 on 2023-06-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutMe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='img',
            field=models.CharField(default='https://steamuserimages-a.akamaihd.net/ugc/204179658730228724/7DA3284CED8D923FECBC5BBB11D021B5842FE4A0/', max_length=500),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='img',
            field=models.CharField(default='https://steamuserimages-a.akamaihd.net/ugc/204179658730228724/7DA3284CED8D923FECBC5BBB11D021B5842FE4A0/', max_length=500),
        ),
    ]
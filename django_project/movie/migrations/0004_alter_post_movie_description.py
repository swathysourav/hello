# Generated by Django 4.2.10 on 2024-02-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_post_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='movie_description',
            field=models.TextField(null=True),
        ),
    ]
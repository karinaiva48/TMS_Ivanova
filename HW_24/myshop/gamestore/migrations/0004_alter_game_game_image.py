# Generated by Django 4.1.7 on 2023-03-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamestore", "0003_alter_game_game_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="game_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]

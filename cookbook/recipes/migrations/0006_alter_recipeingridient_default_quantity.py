# Generated by Django 4.1.5 on 2023-01-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_step_recipe_image_delete_steps_step_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingridient',
            name='default_quantity',
            field=models.FloatField(),
        ),
    ]

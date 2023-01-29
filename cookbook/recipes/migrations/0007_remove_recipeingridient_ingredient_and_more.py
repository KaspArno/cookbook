# Generated by Django 4.1.5 on 2023-01-29 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipeingridient_default_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingridient',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipeingridient',
            name='ingredient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient'),
            preserve_default=False,
        ),
    ]
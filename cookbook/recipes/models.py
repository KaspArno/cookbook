from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    time = models.DurationField(null=True, blank=True)
    defult_portions = models.IntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name 

class RecipeIngridient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    default_quantity = models.FloatField()

    def __str__(self):
        return F"{self.recipe.name}: {self.default_quantity} {self.ingredient.name}"

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.recipe.name}: step {self.number}"
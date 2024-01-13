from django.shortcuts import render
from django.views import generic

from recipes.models import Recipe

# Create your views here.

class RecipesListView(generic.ListView):
    model = Recipe

class RecipesDetailView(generic.DetailView):
    model = Recipe
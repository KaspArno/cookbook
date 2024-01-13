from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.RecipesListView.as_view(), name="index"),
    path("recipes/<int:pk>/", views.RecipesDetailView.as_view(), name="detail")
]
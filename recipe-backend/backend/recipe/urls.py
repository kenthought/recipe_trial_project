from django.urls import path
from recipe.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", RecipeList.as_view(), name="recipe"),
    path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("user/<int:user>/", UserRecipeList.as_view()),
    path("user/<int:user>/<int:pk>/", UserRecipeDetail.as_view(), name="user_recipe_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

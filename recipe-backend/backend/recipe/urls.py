from django.urls import path
from recipe.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", RecipeList.as_view()),
    path("<int:pk>/", RecipeDetail.as_view()),
    path("user/<int:user>/", UserRecipeList.as_view()),
    path("user/<int:user>/<int:pk>/", UserRecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

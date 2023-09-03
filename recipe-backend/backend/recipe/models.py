from django.db import models
from django.conf import settings


# Create your models here.
class Recipe(models.Model):
    recipe = models.CharField(
         max_length=100, 
    )
    ingredients = models.CharField(max_length=1500)
    instructions = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="recipe", on_delete=models.PROTECT
    )

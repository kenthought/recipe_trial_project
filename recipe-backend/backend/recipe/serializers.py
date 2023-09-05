from rest_framework import serializers
from .models import Recipe
from users.serializers import UserSerializer

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['recipe', 'ingredients', 'instructions', 'user']
    
class RecipeViewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Recipe
        fields = ['id', 'recipe', 'ingredients', 'instructions', 'user']

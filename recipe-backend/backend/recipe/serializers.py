from rest_framework import serializers
from .models import Recipe
from users.serializers import UserSerializer

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['recipe', 'ingredients', 'instructions', 'user']

    # def create(self, validated_data):
    #     return self.Meta.model(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.recipe = validated_data.get('recipe', instance.recipe)
    #     instance.ingredients = validated_data.get('ingredients', instance.ingredients)
    #     instance.instructions = validated_data.get('instructions', instance.instructions)
    #     instance.user = validated_data.get('user', instance.user)
    #     return instance
    
class RecipeViewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Recipe
        fields = ['id', 'recipe', 'ingredients', 'instructions', 'user']

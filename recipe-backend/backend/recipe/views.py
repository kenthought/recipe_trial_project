from django.shortcuts import render
from recipe.models import Recipe
from recipe.serializers import (
    RecipeViewSerializer,
    RecipeSerializer,
)
from django.http import Http404
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

    
class RecipeList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        recipe = Recipe.objects.all()
        serializer = RecipeViewSerializer(recipe, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(APIView):
    permissions_clases = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeViewSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Fetch user recipes
class RecipeUserList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user):
        try:
            return Recipe.objects.filter(user_id=user)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, user, format=None):
        recipe = self.get_object( user)
        serializer = RecipeViewSerializer(recipe, many=True)
        return Response(serializer.data)


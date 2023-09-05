import json

from users.models import UserManager, UserData
from django.test import TestCase
from django.urls import reverse
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

# Create your tests here.
class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "testcase@test.com", "email": "testcase@test.com",
            "password": "Test@231!", "first_name": "Test", "middle_name": "Tester",
            "last_name":"Chan"
            }
        response = self.client.post("/api/users/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class RecipeTestCase(APITestCase):

    recipe_url = reverse("recipe")

    def setUp(self):
        self.user = UserData.objects.create_user(
            email="testcase1@test.com",
            username="testcase1@test.com",
            password= "Test@231!", 
            first_name= "Test1", 
            middle_name= "Tester",
            last_name= "Chan"
            )
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token))

    def test_post_recipe_authenticated(self):
        data = {
            "recipe":"Adobo", "ingredients":"Test", 
            "instructions":"Test", "user": self.user.id
            }
        response = self.client.post(self.recipe_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_recipe_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "recipe":"Sinigang", "ingredients":"Test", 
            "instructions":"Test", "user": self.user.id
            }
        response = self.client.post(self.recipe_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_recipe_list_authenticated(self):
        response = self.client.get(self.recipe_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recipe_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.recipe_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        
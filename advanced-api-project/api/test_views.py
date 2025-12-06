from django.contrib.auth.models import User, AnonymousUser
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from .views import CreateView, UpdateView, DeleteView


class BookTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="mockuser", email="mockuser@test.com", password="mock_password")
        self.author_one = Author.objects.create(name= "author_one")
        self.author_two = Author.objects.create(name= "author_two")
        self.author_three = Author.objects.create(name= "author_three")


    def test_create_book(self):

        data = {
            "title": "first_book",
            "publication_year": 2020,
            "author": self.author_one
        }
        self.client.login(username="mockuser", password="mock_password")
        response = self.client.post("/books/create", data= data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_update_book(self):

        to_update = {
            "publication_year": 2018
        }
        self.client.login(username="mockuser", password="mock_password")
        response = self.client.put("/books/update/1", data= to_update)

        self.assertEqual(response.data["publication_year"], 2018)
    
    def test_delete_book(self):

        self.client.login(username="mockuser", password="mock_password")
        response = self.factory.delete("/books/delete/1")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

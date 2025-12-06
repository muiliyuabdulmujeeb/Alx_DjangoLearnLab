from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase, RequestFactory
from .models import Author, Book
from .views import CreateView, UpdateView, DeleteView


class BookTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
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
        request = self.factory.post("/books/create", data= data)
        request.user = self.user

        response = CreateView.as_view()(request)

        self.assertEqual(response.status_code, 201)

    
    def test_update_book(self):

        to_update = {
            "publication_year": 2018
        }

        request = self.factory.put("/books/update/1", data= to_update)
        request.user = self.user

        response = UpdateView.as_view()(request)

        self.assertEqual(response.content.publication_year, 2018)
    
    def test_delete_book(self):
        request = self.factory.delete("/books/delete/1")
        request.user = self.user

        response = DeleteView.as_view()(request)

        self.assertEqual(response.content, None)

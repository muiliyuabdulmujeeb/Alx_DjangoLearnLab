from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class ListView(generics.ListAPIView):
    """ for listing all books in the database, with permissions and can be filtered, ordered and also has search capabilities"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends =[rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author"]
    ordering_fields = ["title", "publication_year"]

class DetailView(generics.RetrieveAPIView):
    """ for getting the details of a particular book"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    """ for creating a book instance"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    """ for updating a book instance"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    """ for deleting a book instance"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
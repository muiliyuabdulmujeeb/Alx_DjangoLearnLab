from datetime import datetime
from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """BookSerializer to serialize all books and make sure created book publication year is not in the future"""
    class Meta:
        model= Book
        fields= "__all__"

    def validate(self, data):
        publication_year = data.get("publication_year")
        if publication_year is not None:
            if publication_year > datetime.year:
                raise serializers.ValidationError("cannot set a future year")
        else:
            raise serializers.ValidationError("publication year cannot be empty")

class AuthorSerializer(serializers.ModelSerializer):
    """Author serializer that takes into account the books each author has"""
    books = BookSerializer(many= True)

    class Meta:
        model= Author
        fields= ['name', 'books']
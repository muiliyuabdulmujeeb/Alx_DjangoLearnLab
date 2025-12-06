from django.db import models

# Create your models here.

class Author(models.Model):

    """Author model"""
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name
    

class Book(models.Model):

    """Book model that is related to Author in a one to many way"""
    title = models.CharField(max_length= 150)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete= models.CASCADE)


    def __str__(self):
        return self.title + "||" + self.publication_year
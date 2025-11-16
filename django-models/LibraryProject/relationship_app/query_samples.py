from .models import Author, Book, Library, Librarian



#query all books by a specific author
author_name = "James St. Patrick"
author= Author.objects.get(name=author_name)
books= Book.objects.filter(author=author)
books.all()

#list all books in a library
library_name = "alx_library"
Library.objects.get(name=library_name)



#retrieve the librarian for a library
library_name = "alx_library"
Librarian.objects.get(library__name=library_name)
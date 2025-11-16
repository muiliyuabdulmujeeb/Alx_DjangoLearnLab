from .models import Book, Library, Librarian



#query all books by a specific author
author_name = "James St. Patrick"
books= Book.objects.filter(author__name=author_name)
books.all()

#list all books in a library
library_name = "alx_library"
Library.objects.get(name=library_name)



#retrieve the librarian for a library
library_name = "alx_library"
Librarian.objects.get(library__name=library_name)
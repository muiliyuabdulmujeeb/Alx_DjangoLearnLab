from .models import Book, Library, Librarian



#query all books by a specific author
author_name = "James St. Patrick"
books_by_author = Book.objects.filter(author__name= author_name)

#list all books in a library
library_name = "alx_library"
library = Library.objects.get(name= library_name)
for value in library:
    value.books.all()


#retrieve the librarian for a library
library_name = "alx_library"
librarian = Librarian.objects.get(library__name= library_name)
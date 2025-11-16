from .models import Book, Library, Librarian



#query all books by a specific author
books_by_author = Book.objects.filter(author__name= "James St. Patrick")

#list all books in a library
library = Library.objects.filter(name= "alx_library")
for value in library:
    value.books.all()


#retrieve the librarian for a library
librarian = Librarian.objects.get(library__name= "alx_library")
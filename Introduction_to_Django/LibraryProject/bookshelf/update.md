python command:
```
from bookshelf.models import Book

book = Book.objects.get(id= 2)
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)
```

response: Nineteen Eighty-Four

comment: using `Book.objects.get(id= 2)`, raises an error while using the id doesnt. The new title was printed to confirm it works.
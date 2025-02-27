from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Author, Book
from .serializers import (CreateAuthorSerializer, CreateBookSerializer, DeleteAuthorSerializer,
    DeleteBookSerializer, ListAuthorsSerializer, ListBooksSerializer, UpdateAuthorSerializer,
    UpdateBookSerializer)
from django.db.models import Count
# Create your views here.
class LibraryViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == "create_book":
            return CreateBookSerializer
        elif self.action == "create_author":
            return CreateAuthorSerializer
        elif (self.action == "retrieve_books"):
            return ListBooksSerializer
        elif (self.action == "retrieve_author"):
            return ListAuthorsSerializer
        elif (self.action == "update_books"):
            return UpdateBookSerializer
        elif (self.action == "retrieve_book_by_id"):
            return ListBooksSerializer
        elif (self.action == "update_author"):
            return UpdateAuthorSerializer
        elif (self.action == "retrieve_author_by_id"):
            return ListAuthorsSerializer
        elif (self.action == "delete_book"):
            return DeleteBookSerializer
        elif (self.action == "delete_author"):
            return DeleteAuthorSerializer
        elif (self.action == "ranking_authors"):
            return ListAuthorsSerializer
        return ListBooksSerializer
    
    def create_book(self, request):
        """
        Purpose: Cria um novo livro
        """
        book_serializer = self.get_serializer(data=request.data)
        if book_serializer.is_valid():
            book = book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create_author(self, request):
        """
        Purpose: Cria um novo autor
        """
        author_serializer = self.get_serializer(data=request.data)
        if author_serializer.is_valid():  
            author = author_serializer.save()
            print(author)
            return Response(author_serializer.data, status=status.HTTP_201_CREATED)
        return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve_author(self, request):
        authors = Author.objects.all()
        author_serializer = self.get_serializer(authors, many=True)
        return Response(author_serializer.data, status=status.HTTP_200_OK)
    def retrieve_books(self, request):
        books = Book.objects.all()
        book_serializer = self.get_serializer(books, many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    def update_books(self, request, pk=None, **kwargs):
        try:
            book = Book.objects.get(pk=pk)
            book_serializer = self.get_serializer(book, data=request.data, partial=True)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response(book_serializer.data, status=status.HTTP_200_OK)
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Book.DoesNotExist:
            return Response({"detail": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    def retrieve_book_by_id(self, request, pk=None, **kwargs):
        """
        Purpose: Lista livro pelo id
        """
        try:
            book = Book.objects.get(pk=pk)
            book_serializer = self.get_serializer(book)
            
            return Response(book_serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"detail": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    def retrieve_author_by_id(self, request, pk=None, **kwargs):
        """
        Purpose: Lista autor pelo id
        """
        try:
            author = Author.objects.get(pk=pk)
            author_serializer = self.get_serializer(author)
            
            return Response(author_serializer.data, status=status.HTTP_200_OK)
        except author.DoesNotExist:
            return Response({"detail": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    def update_author(self, request, pk=None, **kwargs):
        try:
            author = Author.objects.get(pk=pk)
            author_serializer = self.get_serializer(author, data=request.data, partial=True)
            if author_serializer.is_valid():
                author_serializer.save()
                return Response(author_serializer.data, status=status.HTTP_200_OK)
            return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Author.DoesNotExist:
            return Response({"detail": "Autor não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    def delete_book(self, request, pk=None):
        """
        Purpose: Remove um livro específico pelo UUID
        """
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"detail": "Livro removido com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"detail": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete_author(self, request, pk=None):
        """
        Purpose: Remove um autor específico pelo UUID
        """
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return Response({"detail": "Autor removido com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response({"detail": "Autor não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
    def ranking_authors(self, request):
        """
        Purpose: Retorna os 5 autores com mais de 5 livros publicados.
        """
        books_authors = Author.objects.annotate(book_count=Count('book')).filter(book_count__gt=5).order_by('-book_count')[:5]

        ranking_best_authors = [
            {
                "id": author.id,
                "name": author.name,
                "book_count": author.book_count
            }
            for author in books_authors
        ]

        return Response(ranking_best_authors, status=status.HTTP_200_OK)
# library/urls.py
from django.urls import path
from .views import LibraryViewSet

urlpatterns = [
    path("author/", LibraryViewSet.as_view({
        'get': 'retrieve_author',
        'post': 'create_author'
    }), name="author"),
    
    path("book/", LibraryViewSet.as_view({
        'get': 'retrieve_books',
        'post': 'create_book'
        }), name="books"),
        path("book/<uuid:pk>/", LibraryViewSet.as_view({
        'get': 'retrieve_book_by_id',
        'put': 'update_books', 
        'patch': 'update_books',
        'delete': 'delete_book'
    }), name="author-detail"),
    path("author/<uuid:pk>/", LibraryViewSet.as_view({
        'get': 'retrieve_author_by_id',
        'put': 'update_author', 
        'patch': 'update_author',
        'delete': 'delete_author'
    }), name="author-detail"),
]
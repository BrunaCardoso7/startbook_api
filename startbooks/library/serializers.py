from rest_framework import serializers
from .models import Author, Book

class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']  
class ListAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date'] 

class ListBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  
class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date'] 
        
class UpdateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name'] 
class DeleteAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id'] 
        
class DeleteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id'] 
from django.db import models

class Author(models.Model):
    name= models.CharField(max_length=100, null=True, blank=True)
# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateTimeField(null=True)
    author= models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE)
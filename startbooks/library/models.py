from django.db import models
import uuid
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateTimeField(null=True)
    author= models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE)

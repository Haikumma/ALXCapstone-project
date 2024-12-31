from django.db import models

#book model 
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    number_of_copies = models.PositiveIntegerField()
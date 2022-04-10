from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', args=(self.id,))

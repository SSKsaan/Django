from django.db import models

# Author model with a unique 'username' field (used for SlugRelatedField)
class Author(models.Model):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Book model with foreign key to Author and a write-only field for secret info
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    secret_note = models.TextField(default="classified")

    def __str__(self):
        return self.title

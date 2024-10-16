# models.py
from django.db import models


class User(models.Model):
    LIBRARIAN = 'librarian'
    PATRON = 'patron'

    ROLE_CHOICES = [
        (LIBRARIAN, 'Librarian'),
        (PATRON, 'Patron'),
    ]

    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default=PATRON)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/images/', blank=True, null=True)  # Use ImageField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


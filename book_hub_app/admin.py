from django.contrib import admin
from .models import User, Book

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role')  # Customize the columns to display
    search_fields = ('username', 'email')  # Add search functionality
    list_filter = ('role',)  # Enable filtering by role

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'created_at')  # Customize the columns to display
    search_fields = ('title', 'author', 'isbn')  # Add search functionality
    list_filter = ('author',)  # Enable filtering by author



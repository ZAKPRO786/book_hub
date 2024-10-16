from rest_framework import serializers
from .models import User, Book


class UserSerializer(serializers.ModelSerializer):
    # Optionally, you can customize validation and add read-only fields here
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']  # Ensure 'role' is defined in your model

    # Example of adding custom validation for the email field
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'image', 'created_at']

    # You can also add custom validation if needed
    def validate_isbn(self, value):
        if len(value) not in [10, 13]:  # Example validation for ISBN length
            raise serializers.ValidationError("ISBN must be either 10 or 13 characters long.")
        return value

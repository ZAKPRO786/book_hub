from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import User, Book
from .serializers import UserSerializer, BookSerializer
from django.db.models import Q  # For search functionality
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

class UserView(APIView):
    # Retrieve all users or a single user by ID
    def get(self, request, pk=None):
        query = request.query_params.get('q', None)  # Capture search query parameter
        if pk:
            logger.info(f"Fetching user with id: {pk}")
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)
        elif query:
            logger.info(f"Searching users with query: {query}")
            users = User.objects.filter(
                Q(username__icontains=query) | Q(email__icontains=query)  # Search by username or email
            )
            serializer = UserSerializer(users, many=True)
        else:
            logger.info("Fetching all users")
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # Create a new user
    def post(self, request):
        logger.info(f"Creating new user with data: {request.data}")
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Error creating user: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update a user by ID
    def put(self, request, pk):
        logger.info(f"Updating user with id: {pk}")
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)

        # Check if email is being changed
        new_email = request.data.get('email')
        if new_email and new_email != user.email:
            # Validate if the new email already exists
            if User.objects.filter(email=new_email).exists():
                logger.error("Email already in use")
                return Response({"email": ["This email is already in use."]}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f"Error updating user: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a user by ID
    def delete(self, request, pk):
        logger.info(f"Deleting user with id: {pk}")
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BookView(APIView):
    # Retrieve all books or a single book by ID
    def get(self, request, pk=None):
        query = request.query_params.get('q', None)  # Capture search query parameter
        if pk:
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book)
        elif query:
            logger.info(f"Searching books with query: {query}")
            books = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query)
            )
            serializer = BookSerializer(books, many=True)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # Create a new book
    def post(self, request):
        logger.info(f"Creating new book with data: {request.data}")
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Error creating book: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update a book by ID
    def put(self, request, pk):
        logger.info(f"Updating book with id: {pk}")
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f"Error updating book: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a book by ID
    def delete(self, request, pk):
        logger.info(f"Deleting book with id: {pk}")
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


def test_media_view(request):
    html = '''
    <h1>Media Files Test</h1>
    <ul>
        <li><a href="/media/books/images/Screenshot_2024-10-15_214042.png">Screenshot</a></li>
        <li><a href="/media/books/images/The_Great_Gatsby_Cover_1925_Retouched.jpg">The Great Gatsby Cover</a></li>
    </ul>
    '''
    return HttpResponse(html)

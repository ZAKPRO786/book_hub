from django.urls import path
from .views import UserView, BookView,test_media_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),        # List or Create Users
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),  # Get, Update, Delete Users by ID
    path('books/', BookView.as_view(), name='book-list'),        # List or Create Books
    path('books/<int:pk>/', BookView.as_view(), name='book-detail'),
    path('test-media/', test_media_view, name='test_media'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from rest_framework import routers
from .views import AuthorViewSet

# urlpatterns = [
#     path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
#     path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),
#     path('books/', BookListCreateView.as_view(), name='book-list-create'),
#     path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
# ]

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = router.urls

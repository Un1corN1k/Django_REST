from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from .views import AuthorViewSet
from .views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView, BookListCreateView, \
    BookRetrieveUpdateDestroyView, PurchaseViewSet, ReturnViewSet

router = routers.DefaultRouter()
router.register(r'purchases', PurchaseViewSet)
router.register(r'returns', ReturnViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]

# router = routers.DefaultRouter()
# router.register(r'authors', AuthorViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

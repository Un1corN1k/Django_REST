from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Author, Book, Purchase, Return
from .filters import PurchaseFilter
from .serializers import AuthorSerializer, BookSerializer, PurchaseSerializer, ReturnSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken


class AuthorListCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.save()
        refresh = RefreshToken.for_user(author)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

    def get_queryset(self):
        queryset = super().get_queryset()
        book_name = self.request.query_params.get('book_name')

        if book_name:
            queryset = queryset.filter(book__title__icontains=book_name)

        return queryset.distinct()


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        author_age = self.request.query_params.get('author_age')

        if author_age and author_age.isdigit():
            queryset = queryset.filter(author__age__gte=int(author_age))

        return queryset


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        author = self.get_object()
        book_ids = author.book_set.values_list('id', flat=True)
        return Response({'books': book_ids})


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and not user.is_superuser:
            return Purchase.objects.filter(user=user)
        else:
            return super().get_queryset()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        else:
            return []


class ReturnViewSet(viewsets.ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

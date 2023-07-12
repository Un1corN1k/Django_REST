import django_filters
from django.contrib.auth.models import User
from .models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user__username': ['exact'],
        }

    def filter_queryset(self, queryset):
        request = self.request
        user = request.user
        if not user.is_superuser and user.is_authenticated:
            queryset = queryset.filter(user=user)
        return super().filter_queryset(queryset)


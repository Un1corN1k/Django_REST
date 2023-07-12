from rest_framework import serializers
from .models import Author, Book, Purchase, Return


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        validated_data['title'] += "!"
        return super().create(validated_data)


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'product_name', 'quantity', 'price', "user", 'created_at')


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = ('id', 'purchase', 'reason', 'created_at')

    def create(self, validated_data):
        purchase = validated_data['purchase']
        reason = validated_data['reason']

        return_obj = Return.objects.create(purchase=purchase, reason=reason)
        purchase.delete()
        return return_obj

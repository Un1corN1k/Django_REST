from rest_framework import serializers
from .models import User, Purchase, Product


class UserSerializer(serializers.ModelSerializer):
    purchases = "PurchaseSerializer(many=True)"

    class Meta:
        model = User
        fields = ['name', 'gender', 'age', 'english_level']

        def validate(self, data):
            gender = data.get('gender')
            age = data.get('age')
            english_level = data.get('english_level')

            if (gender == 'M' and age >= 20 and english_level == 'B2') or (
                gender == 'F' and age >= 22 and english_level > 'B1'):
                return data
            else:
                raise serializers.ValidationError('You do not meet the requirements.')

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            purchases_data = representation.pop('purchases')

            purchases_list = []
            for purchase_data in purchases_data:
                purchase_dict = {
                    'purchase_id': purchase_data['id'],
                    'product': purchase_data['product'],
                    'quantity': purchase_data['quantity'],
                    'date': purchase_data['date']
                }
                purchases_list.append(purchase_dict)

            representation['purchases'] = purchases_list
            return representation

        def create(self, validated_data):
            return User.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'product', 'quantity', 'date']


class PurchaseSerializerForUser(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'product', 'quantity', 'date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product_id = representation['product']
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product)
        representation['product'] = product_serializer.data
        return representation

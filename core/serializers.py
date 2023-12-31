from rest_framework import serializers

from core.models import Product, Category, Stock, History


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("__all__")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("__all__")


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("__all__")

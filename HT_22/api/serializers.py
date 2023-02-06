from rest_framework import serializers

from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.current_price = validated_data.get('current_price', instance.current_price)
        instance.old_price = validated_data.get('old_price', instance.old_price)
        instance.sell_status = validated_data.get('sell_status', instance.sell_status)
        instance.href = validated_data.get('href', instance.href)
        instance.item_id = validated_data.get('item_id', instance.item_id)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_title', 'category_id')

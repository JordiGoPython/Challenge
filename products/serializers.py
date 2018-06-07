from rest_framework import serializers
from products.models import Product, ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = '__all__'
        read_only_fields = ('product',)


class ProductSerializer(serializers.ModelSerializer):
    detail_product = ProductDetailSerializer(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('brand_name', 'family_name', 'type_name', 'detail_product')

    def create(self, validated_data):
        detail_product = validated_data.pop('detail_product')
        product = Product.objects.create(**validated_data)
        ProductDetail.objects.create(product=product, **detail_product)
        return product

    def update(self, instance, validated_data, pk=None):
        detail_product = validated_data.pop('detail_product')
        product = Product.objects.filter(id=instance.id)
        product.update(**validated_data)
        product[0].save()
        pr_obj = Product.objects.get(pk=instance.id)
        if detail_product:
            ProductDetail.objects.filter(product=instance).update(**detail_product)
        return pr_obj


class SetProductsSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)


class CatalogSerializer(serializers.ModelSerializer):
    detail_product = ProductDetailSerializer(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = ('id', 'detail_product', 'name', 'brand_name', 'family_name', 'type_name', 'offer_day_from','offer_day_to','offer_price_offer',)

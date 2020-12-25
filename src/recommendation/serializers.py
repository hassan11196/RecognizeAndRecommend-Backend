from rest_framework.serializers import ModelSerializer
from src.recommendation.models import ProductPrice, Category, ProductImage, ProductFeatureBullet, ProductReviewMetaData, ProductVariant, Product, ProductReview


class ProductPriceSerializer(ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductFeatureBulletSerializer(ModelSerializer):

    class Meta:
        model = ProductFeatureBullet
        fields = '__all__'


class ProductReviewMetaDataSerializer(ModelSerializer):

    class Meta:
        model = ProductReviewMetaData
        fields = '__all__'


class ProductVariantSerializer(ModelSerializer):

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductReviewSerializer(ModelSerializer):

    class Meta:
        model = ProductReview
        fields = '__all__'

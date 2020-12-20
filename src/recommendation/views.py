from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from src.recommendation.serializers import ProductPriceSerializer, CategorySerializer, ProductImageSerializer, ProductFeatureBulletSerializer, ProductReviewMetaDataSerializer, ProductVariantSerializer, ProductSerializer
from src.recommendation.models import ProductPrice, Category, ProductImage, ProductFeatureBullet, ProductReviewMetaData, ProductVariant, Product


class ProductPriceViewSet(ViewSet):

    def list(self, request):
        queryset = ProductPrice.objects.order_by('pk')
        serializer = ProductPriceSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductPriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ProductPrice.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductPriceSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ProductPrice.objects.get(pk=pk)
        except ProductPrice.DoesNotExist:
            return Response(status=404)
        serializer = ProductPriceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ProductPrice.objects.get(pk=pk)
        except ProductPrice.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CategoryViewSet(ViewSet):

    def list(self, request):
        queryset = Category.objects.order_by('pk')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductImageViewSet(ViewSet):

    def list(self, request):
        queryset = ProductImage.objects.order_by('pk')
        serializer = ProductImageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ProductImage.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductImageSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ProductImage.objects.get(pk=pk)
        except ProductImage.DoesNotExist:
            return Response(status=404)
        serializer = ProductImageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ProductImage.objects.get(pk=pk)
        except ProductImage.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductFeatureBulletViewSet(ViewSet):

    def list(self, request):
        queryset = ProductFeatureBullet.objects.order_by('pk')
        serializer = ProductFeatureBulletSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductFeatureBulletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ProductFeatureBullet.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductFeatureBulletSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ProductFeatureBullet.objects.get(pk=pk)
        except ProductFeatureBullet.DoesNotExist:
            return Response(status=404)
        serializer = ProductFeatureBulletSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ProductFeatureBullet.objects.get(pk=pk)
        except ProductFeatureBullet.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductReviewMetaDataViewSet(ViewSet):

    def list(self, request):
        queryset = ProductReviewMetaData.objects.order_by('pk')
        serializer = ProductReviewMetaDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductReviewMetaDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ProductReviewMetaData.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductReviewMetaDataSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ProductReviewMetaData.objects.get(pk=pk)
        except ProductReviewMetaData.DoesNotExist:
            return Response(status=404)
        serializer = ProductReviewMetaDataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ProductReviewMetaData.objects.get(pk=pk)
        except ProductReviewMetaData.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductVariantViewSet(ViewSet):

    def list(self, request):
        queryset = ProductVariant.objects.order_by('pk')
        serializer = ProductVariantSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ProductVariant.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductVariantSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ProductVariant.objects.get(pk=pk)
        except ProductVariant.DoesNotExist:
            return Response(status=404)
        serializer = ProductVariantSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ProductVariant.objects.get(pk=pk)
        except ProductVariant.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductViewSet(ViewSet):

    def list(self, request):
        queryset = Product.objects.order_by('pk')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        serializer = ProductSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

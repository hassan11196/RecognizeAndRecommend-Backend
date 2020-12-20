from django.contrib import admin
from .models import Product, ProductPrice, Category, ProductFeatureBullet, ProductReviewMetaData, ProductVariant
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(Category)
admin.site.register(ProductFeatureBullet)
admin.site.register(ProductReviewMetaData)
admin.site.register(ProductVariant)
from django.urls import path
from rest_framework.routers import SimpleRouter
from src.recommendation import views


router = SimpleRouter()

router.register(r'productprice', views.ProductPriceViewSet, 'ProductPrice')
router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'productimage', views.ProductImageViewSet, 'ProductImage')
router.register(r'productfeaturebullet', views.ProductFeatureBulletViewSet, 'ProductFeatureBullet')
router.register(r'productreviewmetadata', views.ProductReviewMetaDataViewSet, 'ProductReviewMetaData')
router.register(r'productvariant', views.ProductVariantViewSet, 'ProductVariant')
router.register(r'product', views.ProductViewSet, 'Product')
router.register(r'productreview', views.ProductReviewViewSet, 'ProductReview')

urlpatterns = router.urls

urlpatterns += [
    path('recommended-products', views.RecommendedProductApiView.as_view()),
    path('productreview-asin/<str:asin>', views.ProductReviewFromProductIdApiView.as_view())
]
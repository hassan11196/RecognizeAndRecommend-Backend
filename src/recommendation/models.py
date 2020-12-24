from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.


class ProductPrice(models.Model):
    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"

    symbol = models.CharField("symbol", max_length=50, null=True, blank=True)
    currency = models.CharField("currency", max_length=50, null=True, blank=True)
    current_price = models.FloatField("current_price", null=True, blank=True)
    discounted = models.BooleanField("discounted", null=True, blank=True)
    before_price = models.FloatField("before_price", null=True, blank=True)
    savings_amount = models.FloatField("savings_amount", null=True, blank=True)
    savings_percent = models.FloatField("savings_percent", null=True, blank=True)

    def __str__(self):
        return self.symbol + ":" + self.currency

    def get_absolute_url(self):
        return reverse("price_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    category = models.CharField("category", max_length=50)
    url = models.URLField("url", max_length=200)

    def __str__(self):
        return self.category


class ProductImage(models.Model):
    image = models.URLField("image", max_length=200)

    def __str__(self):
        return self.image


class ProductFeatureBullet(models.Model):
    feature_bullet = models.CharField("feature_bullet", max_length=255)

    def __str__(self):
        return self.feature_bullet


class ProductReviewMetaData(models.Model):
    total_reviews = models.IntegerField("total_reviews", null=True, blank=True)
    rating = models.FloatField("rating", null=True, blank=True)
    answered_questions = models.IntegerField("answered_questions", null=True, blank=True)

    def __str__(self):
        return self.total_reviews


class ProductVariant(models.Model):
    """Model definition for ProductVariant."""
    # TODO: Define fields here
    asin = models.CharField("asin", primary_key=True, max_length=50)
    variant = models.CharField("variant", max_length=50)
    large_image = models.URLField("large_image", max_length=200)

    class Meta:
        """Meta definition for ProductVariant."""

        verbose_name = 'ProductVariant'

        verbose_name_plural = 'ProductVariants'

    def __str__(self):
        """Unicode representation of ProductVariant."""
        return self.asin + ":" + self.variant


class Product(models.Model):
    asin = models.CharField("asin", primary_key=True, max_length=50)
    sid = models.CharField("sid", max_length=50, null=True, blank=True)
    title = models.CharField(name='title', max_length=50, null=True, blank=True)
    description = models.TextField("description", null=True, blank=True)
    categories = models.ManyToManyField("recommendation.Category", verbose_name="categories")
    delivery_message = models.CharField("delivery_message", max_length=50, null=True, blank=True)
    images = models.ManyToManyField("recommendation.ProductImage", verbose_name="ProductImages")
    feature_bullets = models.ManyToManyField("recommendation.ProductFeatureBullet",
                                             verbose_name="ProductFeatureBullets",
                                             null=True,
                                             blank=True)
    item_available = models.BooleanField("item_available", null=True, blank=True)
    main_image = models.URLField("main_image", max_length=200, null=True, blank=True)
    also_bought = models.ManyToManyField("recommendation.Product")
    variants = models.ManyToManyField("recommendation.ProductVariant")
    reviews = models.ManyToManyField("recommendation.ProductReviewMetaData")
    price = models.ForeignKey("recommendation.ProductPrice", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.asin + ":" + self.title

    def createProduct(product_json):
        product = Product()

        product.asin = product_json['asin']
        product.sid = product_json['sid']
        product.title = product_json['title']
        product.description = product_json['description']
        product.description = product_json['description']
        product.item_available = product_json['item_available']
        product.main_image = product_json['main_image']

        for categ in product_json['categories']:
            category, created = Category.objects.get_or_create(category=categ['category'], url=categ['url'])
            product.categories.add(category)

        for img in product_json['images']:
            productImage, created = ProductImage.objects.get_or_create(image=img)
            product.images.add(productImage)

        for img in product_json['image']:
            productImage, created = ProductImage.objects.get_or_create(image=img)
            product.images.add(productImage)

        for bullet in product_json['feature_bullets']:
            productFeatureBullet, created = ProductFeatureBullet.objects.get_or_create(feature_bullet=bullet)
            product.feature_bullets.add(productFeatureBullet)

        for relatedProduct in product_json['also_bought']:
            alsoBoughtProduct = cls.createProduct(relatedProduct)
            product.also_bought.add(alsoBoughtProduct)

        productPrice, created = ProductPrice.objects.get_or_create(**product_json['price'])
        product.price = productPrice

        return product


class ProductReview(models.Model):
    rating = models.FloatField(null=True, blank=True)
    verified = models.BooleanField(null=True, blank=True)
    reviewTime = models.CharField(max_length=255, null=True, blank=True)
    asin = models.ForeignKey("recommendation.Product", on_delete=models.SET_NULL, null=True, blank=True)
    reviewerID = models.CharField(max_length=255, null=True, blank=True)
    reviewerName = models.CharField(max_length=255, null=True, blank=True)
    reviewText = models.TextField(null=True, blank=True)
    summary = models.CharField(max_length=255, null=True, blank=True)

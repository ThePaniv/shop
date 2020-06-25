from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    rating = models.IntegerField()
    image = models.ImageField()

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Basket(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    total_price = models.FloatField()
    num_of_products = models.IntegerField()


class BasketStorage(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __repr__(self):
        return 'Basket ID: {}, Product ID: {}'.format(self.basket_id, self.product_id)

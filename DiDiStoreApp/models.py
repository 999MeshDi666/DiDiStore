from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


class Author(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Book(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    page = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    desc = models.TextField(max_length=255)
    authors = models.ManyToManyField(Author)
    publishers = models.ManyToManyField("Publisher")
    categories = models.ForeignKey(Category, on_delete=models.PROTECT)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


class Orders(models.Model):
    order_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book)
    customers = models.ForeignKey("Customer",on_delete=models.PROTECT)
    payments = models.ForeignKey("Payments", on_delete=models.PROTECT)


class Customer(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Payments(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
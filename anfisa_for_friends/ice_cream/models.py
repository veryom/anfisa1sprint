from django.db import models


# Обёртки
class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)


# Топпинги
class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(default=True)


# Сорта мороженного
class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


# Категории
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(default=True)

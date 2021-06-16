from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    weight = models.PositiveSmallIntegerField(default=100, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    def __str__(self):
        return self.title

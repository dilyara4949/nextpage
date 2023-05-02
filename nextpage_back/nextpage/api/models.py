from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()

class Category(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }




class Book(models.Model):
    def __str__(self):
        return f'{self.id}  {self.title}'
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.IntegerField()
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'category': self.category.name,
            'description': self.description,
            'pages': self.pages
        }

class Rating(models.Model) :
    def __str__(self):
        return f'{self.count}'
    count = models.IntegerField()  # count of voted users
    sum = models.FloatField()  # sum of given ratings
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
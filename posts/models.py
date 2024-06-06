from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # a post can be of multiple categories and a category can contain multiple many posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
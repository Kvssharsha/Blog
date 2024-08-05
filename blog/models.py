# Create your models here.
# blog/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

# blog/models.py

# ...

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

class Meta:
    verbose_name_plural = "categories"

def __str__(self):
    return self.name

def __str__(self):
    return self.title

def __str__(self):
    return f"{self.author} on '{self.post}'"
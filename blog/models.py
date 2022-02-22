from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .managers import PostManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'

    OPTIONS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(
        OPTIONS_CHOICES), default='draft')

    objects = PostManager()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

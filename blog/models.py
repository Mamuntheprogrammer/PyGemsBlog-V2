from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.status.PUBLISHED)

class Post(models.Model):
    class status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=status.choices, default=status.DRAFT)
    show_facets = admin.ShowFacets.ALWAYS
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The custom manager


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published']),
        ]

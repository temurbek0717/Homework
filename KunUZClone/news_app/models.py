from django.db import models
from django.utils import timezone
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        Published = 'PB','Published'

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='news/image')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now())
    created_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title
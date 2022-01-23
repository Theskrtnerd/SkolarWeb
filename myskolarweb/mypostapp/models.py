from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Post(models.Model):
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    titleimg = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True, max_length=200)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Category, blank=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)

        super(Post, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

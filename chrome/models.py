from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    STATUS_CHOISES=(
        ('p','publish'),
        ('d','draft')
    )
    
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to='Images787')
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHOISES)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Importiere das User-Modell
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover_file = models.FileField(upload_to='covers', default='covers/default.jpg')
    video_file_1080p = models.FileField(upload_to='videos',default='videos/default.mp4', )
    video_file_720p = models.FileField(upload_to='videos', blank=True, null=True)
    video_file_480p = models.FileField(upload_to='videos', blank=True, null=True)
    genre = models.CharField(max_length=80, default=0)
    uploaded_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    is_public = models.BooleanField(default=False)  # Neues Feld für öffentliche Videos

    def __str__(self):
        return self.title
    
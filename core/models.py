from django.db import models

# class Media(models.Model):
#     MEDIA_TYPES = [
#         ('video', 'Vidéo'),
#         ('photo', 'Photo'),
#         ('doc', 'Document')
#     ]
#     title = models.CharField(max_length=255)
#     media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
#     # Pour une vidéo (YouTube), on stocke une URL iframe ou lien
#     video_url = models.URLField(blank=True, null=True)
#     # Pour une photo
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     # Pour un doc
#     file = models.FileField(upload_to='documents/', blank=True, null=True)
#
#     def __str__(self):
#         return self.title
# class Media(models.Model):
#     MEDIA_TYPES = [
#         ('video', 'Vidéo'),
#         ('photo', 'Photo'),
#         ('doc', 'Document')
#     ]
#     title = models.CharField(max_length=255)
#     media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
#     video_file = models.FileField(upload_to='videos/', blank=True, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     file = models.FileField(upload_to='documents/', blank=True, null=True)
#
#     def __str__(self):
#         return self.title
from django.db import models

# class Media(models.Model):
#     MEDIA_TYPES = [
#         ('video', 'Vidéo'),
#         ('photo', 'Photo'),
#         ('doc', 'Document')
#     ]
#     title = models.CharField(max_length=255)
#     media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
#     video_file = models.FileField(upload_to='videos/', blank=True, null=True)
#     video_url = models.URLField(blank=True, null=True)  # Pour les vidéos par URL
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     file = models.FileField(upload_to='documents/', blank=True, null=True)
#
#     def __str__(self):
#         return self.title

from urllib.parse import urlparse, parse_qs

from django.db import models
from urllib.parse import urlparse, parse_qs

class Media(models.Model):
    MEDIA_TYPES = [
        ('video', 'Vidéo'),
        ('photo', 'Photo'),
        ('doc', 'Document')
    ]
    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        # Si l'URL contient 'watch?v=', on la convertit
        if self.video_url and 'youtube.com/watch' in self.video_url:
            url_data = urlparse(self.video_url)
            query = parse_qs(url_data.query)
            video_id = query.get("v")
            if video_id:
                return f"https://www.youtube.com/embed/{video_id[0]}"
        return self.video_url

from django.db import models
from django.core.validators import FileExtensionValidator

video_validator = FileExtensionValidator(['mp4'])
image_validator = FileExtensionValidator(['png' , 'jpg'])
# Create your models here.

class HeadlineImage(models.Model):
    image = models.ImageField(upload_to='headline' , validators=[image_validator])
    
    created = models.DateField(auto_now_add=True)

class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/images/" , validators=[image_validator])

    created = models.DateField(auto_now_add=True)


class GalleryVideo(models.Model):
    video = models.FileField(upload_to="gallery/videos/" , validators=[video_validator])

    created = models.DateField(auto_now_add=True)
from django import forms 
from django.forms import FileInput
from .models import GalleryVideo , GalleryImage , HeadlineImage


class VideoForm(forms.ModelForm):
    class Meta:
        model = GalleryVideo
        fields = ('video',)
        widgets = {
            'video': FileInput(attrs={'accept': '.mp4,'})
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('image',)
        widgets = {
            'image': FileInput(attrs={'accept':'.png , .jpg'})
        }

class HeadlineForm(forms.ModelForm):
    class Meta:
        model = HeadlineImage
        fields = ('image',)
        widgets = {
            'image': FileInput(attrs={'accept':'.png , .jpg'})
        }

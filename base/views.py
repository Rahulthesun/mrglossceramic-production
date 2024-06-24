from django.shortcuts import render
from .models import HeadlineImage , GalleryImage , GalleryVideo
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import VideoForm , ImageForm , HeadlineForm

# Create your views here.
def homepage(request):
    image_paths = []
    h_img = HeadlineImage.objects.filter().all()
    context ={
        "images":h_img

    }
    return render(request ,'base/home.html' , context)

def franchise_page(request):
    return render(request, "base/franchise.html")

def image_gallery(request):
    context ={}
    context['images'] = GalleryImage.objects.all()
    return render(request , "base/image_gallery.html" , context)

def video_gallery(request):
    context ={}
    context['videos'] = GalleryVideo.objects.all()
    return render(request , "base/video_gallery.html" , context)

def upload_content(request):
    h_img = HeadlineImage.objects.all()
    context ={
        "headline_images" : h_img
    }
    return render(request, "base/upload_content.html" ,context)

class UploadHeadlineImage(CreateView):
    model= HeadlineImage
    form_class = HeadlineForm
    template_name= "base/headline_image_form.html"
    success_url = reverse_lazy("upload_content")


def gallery_content_upload_img(request):
    context = {}
    images = GalleryImage.objects.all()
    context["images"] = images
    return render(request , "base/gallery_upload_img.html" , context)

def gallery_content_upload_video(request):
    context = {}
    videos = GalleryVideo.objects.all()
    context["videos"] = videos
    return render(request , 'base/gallery_upload_video.html' , context)

class UploadGalleryImage(CreateView):
    model=GalleryImage
    form_class = ImageForm
    template_name= "base/headline_image_form.html"
    success_url = reverse_lazy("gallery_content_image")

class UploadGalleryVideo(CreateView):
    model=GalleryVideo
    form_class = VideoForm
    template_name= "base/headline_image_form.html"
    success_url = reverse_lazy("gallery_content_video")



from django.shortcuts import render
from .models import HeadlineImage , GalleryImage , GalleryVideo 
from django.views.generic import CreateView , DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import VideoForm , ImageForm , HeadlineForm

# Create your views here.

class LoginUser(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('upload_content')
    fields= ['email' , 'password']
    template_name = 'base/login.html'

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

def homepage(request):
    image_paths = []
    h_img = HeadlineImage.objects.all().order_by('created')
    context ={
        "images":h_img

    }
    return render(request ,'base/home.html' , context)

def franchise_page(request):
    return render(request, "base/franchise.html")

def contact_page(request):
    return render(request , 'base/contact.html')

def image_gallery(request):
    context ={}
    context['images'] = GalleryImage.objects.all().order_by('-created')
    return render(request , "base/image_gallery.html" , context)

def video_gallery(request):
    context ={}
    context['videos'] = GalleryVideo.objects.all().order_by('-created')
    return render(request , "base/video_gallery.html" , context)

@login_required
def upload_content(request):
    h_img = HeadlineImage.objects.all().order_by('created')
    context ={
        "headline_images" : h_img
    }
    return render(request, "base/upload_content.html" ,context)

class UploadHeadlineImage(CreateView ,LoginRequiredMixin):
    model= HeadlineImage
    form_class = HeadlineForm
    template_name= "base/headline_image_form.html"
    success_url = reverse_lazy("upload_content")

@login_required
def gallery_content_upload_img(request):
    context = {}
    images = GalleryImage.objects.all().order_by('-created')
    context["images"] = images
    return render(request , "base/gallery_upload_img.html" , context)

@login_required
def gallery_content_upload_video(request):
    context = {}
    videos = GalleryVideo.objects.all().order_by('-created')
    context["videos"] = videos
    return render(request , 'base/gallery_upload_video.html' , context)

class UploadGalleryImage(CreateView , LoginRequiredMixin):
    model=GalleryImage
    form_class = ImageForm
    template_name= "base/headline_image_form.html"
    success_url = reverse_lazy("gallery_content_image")

class UploadGalleryVideo(CreateView , LoginRequiredMixin):
    model=GalleryVideo
    form_class = VideoForm
    template_name= "base/headline_image_form.html"
    success_url = reverse_lazy("gallery_content_video")


class DeleteHeadlineImage(DeleteView , LoginRequiredMixin):
    model=HeadlineImage
    template_name = 'base/confirm_delete.html'
    success_url = reverse_lazy("upload_content")

class DeleteGalleryImage(DeleteView , LoginRequiredMixin):
    model = GalleryImage
    template_name = 'base/confirm_delete.html'
    success_url = reverse_lazy("gallery_content_image")

class DeleteGalleryVideo(DeleteView , LoginRequiredMixin):
    model = GalleryVideo
    template_name = 'base/confirm_delete.html'
    success_url = reverse_lazy("gallery_content_video")

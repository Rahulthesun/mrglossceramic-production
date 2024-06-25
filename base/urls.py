from django.urls import path
from . import views
from .views import UploadHeadlineImage , UploadGalleryVideo , UploadGalleryImage , DeleteHeadlineImage , DeleteGalleryImage , DeleteGalleryVideo , LoginUser
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path("" , views.homepage , name="home"),
    path("login/",LoginUser.as_view() , name='login' ),
    path("franchise_details/" , views.franchise_page , name="franchise"),
    path('contact_page/' , views.contact_page , name="contact"),
    path("image_gallery/" , views.image_gallery , name="image_gallery"),
    path("video_gallery/" , views.video_gallery , name="video_gallery"),
    path("upload_content/" , views.upload_content , name="upload_content"),
    path("upload_headline_image/" , UploadHeadlineImage.as_view() , name="upload_headline_image"),
    path("gallery_content_image/" , views.gallery_content_upload_img , name="gallery_content_image"),
    path("gallery_content_video/" , views.gallery_content_upload_video , name="gallery_content_video"),
    path("upload_gallery_video/" , UploadGalleryVideo.as_view() , name="upload_gallery_video"),
    path("upload_gallery_image/" , UploadGalleryImage.as_view() , name="upload_gallery_image"),
    path('delete_headline_image/<int:pk>/' , DeleteHeadlineImage.as_view() , name='delete_headline_img'),
    path('delete_gallery_image/<int:pk>/' , DeleteGalleryImage.as_view() , name='delete_gallery_img'),
    path('delete_gallery_video/<int:pk>/' , DeleteGalleryVideo.as_view() , name='delete_gallery_video'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
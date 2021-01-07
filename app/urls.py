
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('del_img', views.del_img, name='del_img'),
    # path('', views.img_upload, name='img_upload'),
]

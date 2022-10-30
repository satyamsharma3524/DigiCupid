from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.index,name='index'),
    path('',views.login,name='login'),
    path('editProfile',views.editProfile,name='editProfile'),
    path('userProfile',views.userProfile,name='userProfile')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
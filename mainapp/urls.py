from django.conf.urls import include, url
from django.contrib import admin
from mainapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^index',views.index,name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
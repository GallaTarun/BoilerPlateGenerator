from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

app_name = 'app_generator'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^backend-form/$', views.backendForm, name='backendForm'),
    url(r'^search$', views.searchProjectFolder, name="searchProject"),
    url(r'^setup/download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^setup/(?P<frontend>\w+)-(?P<backend>\w+)', views.setup, name='setup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

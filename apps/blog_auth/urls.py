from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.blog_auth import views


urlpatterns = [
    path('registro/',views.registro, name='registro'),
    path('login/',views.login, name='login'),
    path('cerrar_sesion',views.cerrar_sesion, name='cerrar_sesion'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
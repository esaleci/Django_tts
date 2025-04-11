from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tts_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('convert/', views.convert_text, name='convert'),
    path('history/', views.history, name='history'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

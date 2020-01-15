
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website import views


app_name = 'website'

urlpatterns = [
    path('template/', views.template, name='template'),
    path('', views.home_page , name='homepage'),
    path('catalogue/', views.catalogue , name='catalogue'),
    path('about/', views.about_page , name='about'),
    path('contact/', views.emailView , name='contact'),
    path('FQAs/', views.fqas , name='FQAs')

] + static(settings.STATIC_URL)
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
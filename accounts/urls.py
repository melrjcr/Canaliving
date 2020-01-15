from django.urls import path

from . import views
from .views import profile

app_name = 'accounts'

urlpatterns = [
	path('profile/', profile, name='profile'),
    path('register/', views.Address.as_view(), name='address'),
]
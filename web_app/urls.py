from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.TextItems, name='Text Items'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
]
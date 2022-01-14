from django.urls import path
from . import views


urlpatterns = [
    # Home Route 
    path('', views.home, name='home'),
    # About Route
    path('about/', views.about, name='about'),
    
]
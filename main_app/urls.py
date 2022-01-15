from django.urls import path
from . import views


urlpatterns = [
    # Home Route 
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    # About Route
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('appointment/', views.appointment_index, name='appointment_index'),

]
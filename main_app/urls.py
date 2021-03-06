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
    path('appointment/create/', views.appointment_create_specialty, name='appointment_create_specialty'),
    path('appointment/create/<str:selected_specialty>/', views.appointment_create_doctor, name='appointment_create_doctor'),
    path('appointment/create/<str:selected_specialty>/<int:doctor_id>/', views.appointment_create_appointment, name='appointment_create_appointment'),
    path('appointment/create/<str:selected_specialty>/<int:doctor_id>/submit/', views.appointment_create_submit, name='appointment_create_submit'),
    path('appointment/<int:pk>/delete/', views.AppointmentDelete.as_view(), name="appointment_delete"),
    path('appointment/<int:appointment_id>/update/', views.appointment_update_specialty, name='appointment_update_specialty'),
    path('appointment/<int:appointment_id>/update/<str:selected_specialty>/<int:doctor_id>/', views.appointment_update_appointment, name='appointment_update_appointment'),
    path('appointment/<int:appointment_id>/update/<str:selected_specialty>/', views.appointment_update_doctor, name='appointment_update_doctor'),
    path('appointment/<int:appointment_id>/update/<str:selected_specialty>/<int:doctor_id>/submit/', views.appointment_update_submit, name='appointment_update_submit'),


]
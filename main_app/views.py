from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment, Doctor, Profile


# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def appointment_index(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, "appointment/index.html", {"appointments": appointments})

def appointment_create_specialty(request):
    specialties = []
    unique_specialties = []
    doctors = Doctor.objects.all()
    for doctor in doctors:
        specialties.append(doctor.specialty)
    for specialty in specialties:
        if specialty not in unique_specialties:
            unique_specialties.append(specialty)
    return render(request, "appointment/create.html", {"unique_specialties": unique_specialties})

    
def appointment_create_doctor(request, selected_specialty):
    print(type(selected_specialty))
    doctors = Doctor.objects.filter(specialty = selected_specialty)
    print(doctors)
    return render(request, "appointment/create.html", {"selected_specialty": selected_specialty, "doctors": doctors})

def appointment_create_appointment(request, selected_specialty, doctor_id):
    doctors = Doctor.objects.all().filter(specialty = selected_specialty)
    selected_doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "appointment/create.html", {"selected_specialty": selected_specialty, "selected_doctor": selected_doctor,"doctors": doctors})






    appointments = Appointment.objects.filter(user=request.user)

    return render(request, "appointment/index.html", {"appointments": appointments})
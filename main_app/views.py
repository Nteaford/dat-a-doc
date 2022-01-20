from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


from .models import Appointment, Doctor, Profile


# Create your views here.
def uniquespecialties():
    specialties = []
    unique_specialties = []
    doctors = Doctor.objects.all()
    for doctor in doctors:
        specialties.append(doctor.specialty)
    for specialty in specialties:
        if specialty not in unique_specialties:
            unique_specialties.append(specialty)
    return unique_specialties

class AppointmentUpdate(UpdateView):
  model = Appointment
  fields = ["date", "appointment_reason", "visit_type", "doctor"]

class AppointmentDelete(DeleteView):
  model = Appointment
  success_url = '/appointment/'


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
    uniquespecialties()
    return render(request, "appointment/create.html", {"unique_specialties": uniquespecialties})

    
def appointment_create_doctor(request, selected_specialty):
    uniquespecialties()
    doctors = Doctor.objects.filter(specialty = selected_specialty)
    return render(request, "appointment/create.html", {"selected_specialty": selected_specialty, "doctors": doctors, "unique_specialties": uniquespecialties})

def appointment_create_appointment(request, selected_specialty, doctor_id):
    uniquespecialties()
    doctors = Doctor.objects.all().filter(specialty = selected_specialty)
    selected_doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "appointment/create.html", {"selected_specialty": selected_specialty, "selected_doctor": selected_doctor,"doctors": doctors, "unique_specialties": uniquespecialties})

def appointment_create_submit(request, selected_specialty, doctor_id):
    d = Doctor.objects.get(id=doctor_id)
    a = Appointment.objects.create(
        visit_type=request.POST["visit_type"],
        date=request.POST['date'],
        appointment_reason=request.POST['appointment_reason'],
        user=request.user,
        doctor=d,
    )
    a.save()
    return redirect('appointment_index')


def appointment_update_specialty(request, appointment_id):
    uniquespecialties()
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, "appointment/update.html", {"unique_specialties": uniquespecialties, "appointment": appointment})

    
def appointment_update_doctor(request, selected_specialty, appointment_id):
    uniquespecialties()
    appointment = Appointment.objects.get(id=appointment_id)
    doctors = Doctor.objects.filter(specialty = selected_specialty)
    return render(request, "appointment/update.html", {"selected_specialty": selected_specialty, "doctors": doctors, "unique_specialties": uniquespecialties, "selected_doctor": appointment.doctor, "appointment": appointment})

def appointment_update_appointment(request, appointment_id):
    uniquespecialties()
    appointment = Appointment.objects.get(id=appointment_id)
    selected_specialty = Appointment.objects.get(id=appointment_id).doctor.specialty
    doctors = Doctor.objects.all().filter(specialty = selected_specialty)
    doctor_id = Appointment.objects.get(id=appointment_id).doctor.id
    return render(request, "appointment/update.html", {"selected_specialty": selected_specialty, "selected_doctor": appointment.doctor, "doctor_id": doctor_id, "doctors": doctors, "unique_specialties": uniquespecialties, "appointment": appointment})

def appointment_update_submit(request, appointment_id, selected_specialty, doctor_id):
    d = Doctor.objects.get(id=doctor_id)
    a = Appointment.objects.get(id=appointment_id)
    a.visit_type = request.POST["visit_type"]
    a.date = request.POST["date"]
    a.appointment_reason = request.POST["appointment_reason"]
    a.doctor = d
    a.save()
    return redirect('appointment_index')



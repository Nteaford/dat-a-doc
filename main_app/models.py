import numbers
from types import CoroutineType
from unicodedata import name
from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
from django.contrib.auth.models import User

VISIT_TYPE = (
    ("General", "General Visit"),
    ("Checkup", "Routine Checkup"),
    ("Physical", "Wellness Physical"),
    ("Blood", "Blood Draw / Vaccination"),
    ("Emergency", "Emergency Visit"),
)

STATE = (('AK', 'Alaska'),('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    address_line_1 = models.CharField(max_length=25)
    address_line_2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(
        max_length=2,
        choices=STATE,
        default=STATE[0][0]
    )
    zip = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    med_school =models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    years_practicing = models.IntegerField()
    hospital = models.CharField(max_length=100)
    quote = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    date = models.DateTimeField()
    visit_type = models.CharField(
        max_length=50,
        choices=VISIT_TYPE,
        default=VISIT_TYPE[0][0]
    )
    appointment_reason = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment with ({self.doctor}) on {self.date}"
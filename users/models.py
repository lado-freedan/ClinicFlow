from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Roles(models.TextChoices):
        DOCTOR = "doctor", "Doctor"
        PATIENT = "patient", "Patient"
        STAFF = "staff", "Staff"

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.PATIENT
    )
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    national_id = models.CharField(max_length=10, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, related_name="doctors")
    medical_license_number = models.CharField(max_length=20, unique=True)
    bio = models.TextField(null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}" 
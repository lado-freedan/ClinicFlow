from django.db import models
from django.conf import settings

from users.models import DoctorProfile


class Slot(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="slots")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor', 'start_time', 'end_time')
        ordering = ["start_time"]

    def __str__(self):
        return f"Dr. {self.doctor.user.last_name} | {self.start_time.strftime("%Y-%m-%d %H:%M")}"
    

class Apointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments")
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE, related_name="appointment")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.patient.username} with Dr. {self.slot.doctor.user.last_name} on {self.slot.start_time.strftime("%Y-%m-%d %H:%M")}"
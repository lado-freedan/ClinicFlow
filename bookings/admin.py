from django.contrib import admin

from .models import Slot, Appointment


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("doctor", "start_time", "end_time", "is_booked")
    list_filter = ("is_booked", "doctor")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "slot", "status", "created_at")
    list_filter = ("status", )
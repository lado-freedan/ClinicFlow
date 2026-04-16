from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DoctorProfile, Specialization


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_stasff")
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("role", "phone_number", "national_id")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {"fields": ("role", "phone_number", "national_id")}),
    )


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "specialization", "medical_licence_number", "experience_years")
    search_fields = ("user__username", "medical_licence_number")
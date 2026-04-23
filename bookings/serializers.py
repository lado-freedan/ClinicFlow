from rest_framework import serializers

from .models import Slot
from users.serializers import DoctorSerializer



class SlotSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="doctor.user.first_name")
    last_name = serializers.ReadOnlyField(source="doctor.user.last_name")
    doctor_specialization = serializers.ReadOnlyField(source="doctor.specialization.name")
    class Meta:
        model = Slot
        fields = ["id", "doctor", "first_name", "last_name", "doctor_specialization", "start_time", "end_time", "is_booked"]
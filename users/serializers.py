from rest_framework import serializers

from .models import User, DoctorProfile


class DoctorSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    full_name = serializers.SerializerMethodField()
    specialization = serializers.ReadOnlyField(source="specialization.name")
    
    def get_full_name(self, obj):
        return f"Dr. {obj.user.get_full_name() or obj.user.username}"


    class Meta:
        model = DoctorProfile
        fields = ["id", "first_name", "last_name", "full_name", "specialization"]
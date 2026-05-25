from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .services import create_slots_for_doctor
from .serializers import SlotSerializer
from .models import Slot, Appointment


User = get_user_model()


class SlotCreateView(APIView):
    def post(self, request):
        doctor_id = request.data.get("doctor_id")
        date_str = request.data.get("date")
        start_time_str = request.data.get("start_time")
        end_time_str = request.data.get("end_time")
        duration = request.data.get("duration", 15)

        try:
            slots = create_slots_for_doctor(
                doctor_id=doctor_id,
                date_str=date_str,
                start_time_str=start_time_str,
                end_time_str=end_time_str,
                duration_minutes=int(duration)
            )

            serializer = SlotSerializer(slots, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class AvailableSlotView(ListAPIView):
    serializer_class = SlotSerializer

    def get_queryset(self):
        doctor_id = self.kwargs["doctor_id"]
        return Slot.objects.filter(doctor_id=doctor_id)
    

class BookAppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        slot_id = request.data.get("slot_id")

        try:
            slot = Slot.objects.get(id=slot_id)
        except Slot.DoesNotExist:
            return Response({"error": "slot not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if slot.is_booked:
            return Response({"error": "slot already booked"}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.role != "Patient":
            return Response({"error": "Access denied. Only patients can book."}, status=status.HTTP_403_FORBIDDEN)

        slot.is_booked = True
        slot.save()

        appointment = Appointment.objects.create(
            slot=slot,
            status="PENDING",
            patient=request.user
        )

        return Response({
            "message": "appointment booked successfully",
            "appointment_id": appointment.id
        }, status=status.HTTP_201_CREATED)
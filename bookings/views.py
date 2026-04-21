from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import create_slots_for_doctor
from .serializers import SlotSerializer


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
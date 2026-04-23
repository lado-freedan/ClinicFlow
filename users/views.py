from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import User, DoctorProfile
from .serializers import DoctorSerializer


class DoctorListView(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer
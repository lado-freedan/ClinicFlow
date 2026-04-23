from django.urls import path

from .views import SlotCreateView, AvailableSlotView


urlpatterns = [
    path("slots/create/", SlotCreateView.as_view(), name="slot-create"),
    path("slots/available/<int:doctor_id>/", AvailableSlotView.as_view(), name="available-slots"),
]
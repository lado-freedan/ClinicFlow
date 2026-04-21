from django.urls import path

from .views import SlotCreateView


urlpatterns = [
    path("slots/create/", SlotCreateView.as_view(), name="slot-create"),
]
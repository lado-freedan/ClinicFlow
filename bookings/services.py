from datetime import datetime, timedelta
from django.db import transaction

from .models import Slot
from users.models import DoctorProfile


def create_slots_for_doctor(doctor_id: int, date_str: str, start_time_str:str, end_time_str: str, duration_minuts: int):
    start_dt = datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M")

    slots_to_create = []
    current_time = start_dt

    with transaction.atomic():
        while current_time + timedelta(minuts=duration_minuts) <= end_dt:
            slot_end = current_time + timedelta(minuts=duration_minuts)

            slots_to_create.append(Slot(
                doctor_id=doctor_id,
                start_time=current_time,
                end_time=slot_end
            ))

            current_time = slot_end

        return Slot.objects.bulk_create(slots_to_create)
from django.db import transaction

from .models import User, DoctorProfile


def user_create(username, email, password, role, **extra_fields) ->User:
    with transaction.atomic():
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            **extra_fields
        )

        if role == User.Roles.DOCTOR:
            DoctorProfile.objects.create(user=user)

        return user
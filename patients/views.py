from django.shortcuts import render, redirect
from .models import Treatment, Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

from .utils import send_message
from django.core.mail import send_mail


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")

            return redirect("account_profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "account/profile.html", {"form": form})


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "about.html")


@login_required
def book_appointment(request):
    appointment_form = AppointmentForm(request.POST or None)
    if appointment_form.is_valid():
        edit_appointment_form = appointment_form.save(commit=False)
        edit_appointment_form.user = request.user
        appointment_form.save()
        appointment_form_data = appointment_form.cleaned_data
        appointment_time = appointment_form_data.get("time")
        appointment_description = appointment_form_data.get("description")
        # print("appointment_form_data", appointment_form_data.time)

        docter_name = "Dr. Vikram Sablok"
        message_text_patient = (
            f"Your Appointment Is Booked with {docter_name} at time {appointment_time} "
        )
        message_text_docter = f"You have Appointment Is Booked with {request.user.get_full_name()} at time {appointment_time} and description is {appointment_description}"
        # for patient
        send_mail(
            subject=f"Your Appointment Is Booked With {docter_name}",
            message=message_text_patient,
            from_email="djangopythonjaavs@gmail.com",
            recipient_list=[request.user.email],
            fail_silently=False,
        )
        send_message(message_text_patient, "9503772231")
        # for doctor
        send_mail(
            subject=f"You Have Appointment With {request.user.get_full_name()}",
            message=message_text_docter,
            from_email="djangopythonjaavs@gmail.com",
            recipient_list=["abhishekgawadeprogrammer@gmail.com"],
            fail_silently=False,
        )
        send_message(message_text_docter, "9503772231")
        messages.success(request, f"Your Appointment has been booked!!")
        return redirect("my_appointments")

    context = {"appointment_form": appointment_form}
    return render(request, "appointments.html", context)


@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)

    context = {"appointments": appointments}

    return render(request, "my_appointments.html", context)


def treatments(request):
    treatment_objs = Treatment.objects.all()
    return render(request, "treatments.html", {"treatment_objs": treatment_objs})

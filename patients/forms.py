from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import User, Appointment
from django.utils import timezone


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            "symptoms",
            "time",
            "is_diabetes",
            "previous_treatment_taken",
            "description",
        )
        widgets = {
            "time": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
            ),
            "symptoms": forms.CheckboxSelectMultiple(),
        }

    def clean_time(self):
        if self.cleaned_data["time"] < timezone.now():
            raise forms.ValidationError("Enter the valid time")
        return self.cleaned_data["time"]


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    username = forms.CharField(
        max_length=30,
        label="Phone Number",
        widget=forms.TextInput(attrs={"placeholder": "Phone Number", "type": "number"}),
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

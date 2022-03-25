from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import AbstractUser

from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(
        "Phone Number",
        max_length=10,
        unique=True,
        validators=[
            MinLengthValidator(10),
            RegexValidator(regex=r"^\d*$", message="Only digits are allowed."),
        ],
    )
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=255)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Treatment(models.Model):
    """
    What Treatments the doctor is giving
    """

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TreatmentImage(models.Model):
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="treatment_images/")
    default = models.BooleanField(default=False)


class Appointment(models.Model):
    symptoms = models.ManyToManyField(Treatment)
    time = models.DateTimeField(unique=True)
    is_diabetes = models.BooleanField(default=False)
    previous_treatment_taken = models.BooleanField(default=False)
    description = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_appointment_status(self):
        return self.time > timezone.now()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.user.username + "::" + str(self.description[:20])

    def save(self, *args, **kwargs):
        # item can't  able to sell if they don't have item bags
        print("howq is going to waord")
        super().save(*args, **kwargs)

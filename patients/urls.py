from django.urls import path, include
from .views import about, contactus, treatments, home, book_appointment, my_appointments

urlpatterns = [
    path("about-us/", about, name="about"),
    path("book-appointment/", book_appointment, name="book_appointment"),
    path("my-appointment/", my_appointments, name="my_appointments"),
    path("contact-us/", contactus, name="contactus"),
    path("treatments/", treatments, name="treatments"),
    path("", home, name="home"),
]

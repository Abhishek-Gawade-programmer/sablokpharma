from django.contrib import admin
from .models import Treatment, TreatmentImage, User, Appointment

admin.site.register(Treatment)
admin.site.register(User)
admin.site.register(TreatmentImage)
admin.site.register(Appointment)

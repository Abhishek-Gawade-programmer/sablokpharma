from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from patients.views import profile

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", profile, name="account_profile"),
    path("", include("patients.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

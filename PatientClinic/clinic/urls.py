from django.urls import path
from clinic.views import DoseView

urlpatterns = [
    path("api/<int:machine_id>/", DoseView.as_view(), name="fectch_last_dose")
]
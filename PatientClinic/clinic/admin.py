from django.contrib import admin
from clinic.models import Dose,Machine,Patient


#admin.site.register(Dose)
@admin.register(Dose)
class AppUserAdmin(admin.ModelAdmin):
    """
     Class to manage dose table on admin panel.
    """
    list_display = ["dose_id","dose","patient_id","created","updated"]

@admin.register(Machine)
class AppUserAdmin(admin.ModelAdmin):
    """
     Class to manage machine table on admin panel.
    """
    list_display = ["machine_name","machine_id","created","updated"]

@admin.register(Patient)
class AppUserAdmin(admin.ModelAdmin):
    """
     Class to manage patient table on admin panel.
    """
    list_display = ["patient_name","patient_id","machine_id","created","updated"]

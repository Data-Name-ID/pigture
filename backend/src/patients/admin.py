import django.contrib

import patients.models


@django.contrib.admin.register(patients.models.Patient)
class PatientsAdmin(django.contrib.admin.ModelAdmin):
    list_display = (patients.models.Patient.uuid.field.name,)

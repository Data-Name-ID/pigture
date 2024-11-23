import rest_framework.serializers

import patients.models


class PatientSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = patients.models.Patient
        fields = (patients.models.Patient.uuid.field.name,)

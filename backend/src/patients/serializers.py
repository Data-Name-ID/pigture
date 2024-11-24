import rest_framework.serializers

import patients.models


class PatientSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = patients.models.Patient
        fields = "__all__"

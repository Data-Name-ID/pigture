from rest_framework import viewsets
from rest_framework import decorators
from rest_framework.response import Response

import patients.models
import patients.serializers
import images.serializers
import core.permissions


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = patients.models.Patient.objects.all()
    serializer_class = patients.serializers.PatientSerializer
    permission_classes = [core.permissions.HasGroupPermission]
    required_groups = {
        "GET": ["main_docs", "docs"],
    }

    @decorators.action(methods=["get"], detail=True)
    def images(self, request, pk=None):
        patient = self.get_object()
        images_set = patient.images.all()
        serializer = images.serializers.ImageSerializer(images_set, many=True)
        return Response(serializer.data)

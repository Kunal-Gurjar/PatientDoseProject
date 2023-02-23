from rest_framework.views import APIView
from rest_framework.response import Response
from clinic.serializer import DoseSerializer
from clinic.models import Dose
from rest_framework import status

class DoseView(APIView):
    """
    API view for last Dose.
    """
    def get(self, request, machine_id):
        """
        Method to fetch the last dose.
        :return: last dose instance
        """
        dose_instance = Dose.objects.filter(patient_id__machine_id=machine_id).last()
        serialized_data = DoseSerializer(dose_instance).data
        return Response(serialized_data, status=status.HTTP_200_OK)

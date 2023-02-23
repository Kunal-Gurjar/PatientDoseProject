from rest_framework import serializers


class DoseSerializer(serializers.Serializer):
    """
    Serializer class for Dose Model.
    """
    Machine_id = serializers.SerializerMethodField(method_name="get_machine_id")
    Patient_id = serializers.SerializerMethodField(method_name="get_patient_id")
    Patient_name = serializers.SerializerMethodField(method_name="get_patient_name")
    Dose_id = serializers.IntegerField(source="dose_id")
    Dose = serializers.FloatField(source="dose")

    def get_machine_id(self, inst):
        return inst.patient_id.machine_id.machine_id

    def get_patient_id(self, inst):
        return inst.patient_id.patient_id

    def get_patient_name(self, inst):
        return inst.patient_id.patient_name

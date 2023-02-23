from django.db import models
import uuid


class BaseModel(models.Model):
    """
       Abstract base model.
    """

    class Meta:
        abstract = True

    # Save date and time of add and update.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class PublicId:
    @staticmethod
    def create_public_id():
        return uuid.uuid4().int >> 75


class Machine(BaseModel):
    machine_id = models.IntegerField(primary_key=True, editable=False)
    machine_name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.machine_id:
            self.machine_id = PublicId.create_public_id()
            self.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.machine_name


class Patient(BaseModel):

    patient_id = models.IntegerField(primary_key=True, editable=False)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = PublicId.create_public_id()
            self.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.patient_name

class Dose(BaseModel):
    dose_id = models.AutoField(primary_key=True)
    dose = models.FloatField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)



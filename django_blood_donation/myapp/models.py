from django.db import models

class Donor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.blood_type})"

class BloodRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    blood_type_needed = models.CharField(max_length=5)
    hospital_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
         return f"{self.patient_name} needs {self.blood_type_needed} at {self.hospital_name} (Contact: {self.phone_number})"

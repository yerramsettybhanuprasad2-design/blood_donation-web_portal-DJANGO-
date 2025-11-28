from django.contrib import admin
from .models import Donor, BloodRequest  # Import models

# Register Donor model in Django Admin
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blood_type', 'contact_number', 'city')  # Columns to show in Admin
    search_fields = ('name', 'blood_type', 'city')  # Search functionality

# Register BloodRequest model in Django Admin
@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'blood_type_needed', 'hospital_name', 'city', 'phone_number')  # Fixed field name
    search_fields = ('patient_name', 'blood_type_needed', 'hospital_name', 'city', 'phone_number')  # Fixed field name

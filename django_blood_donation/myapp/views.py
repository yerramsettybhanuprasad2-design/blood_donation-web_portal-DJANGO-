from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Donor, BloodRequest
from django.contrib.admin.views.decorators import staff_member_required

# Home Page
def index(request):
    return render(request, "index.html")

# About Page
def about(request):
    return render(request, "about.html")

# Find Donor Page (Displays all donors)
def find_donor(request):
    blood_type = request.GET.get("blood_type")
    city = request.GET.get("city")
    donors = []

    if blood_type and city:
        donors = Donor.objects.filter(
            blood_type__iexact=blood_type,
            city__icontains=city
        )

    return render(request, "find-donor.html", {
        "donors": donors,
        "query": blood_type,
        "city_query": city
    })

# Blood Request Page (Handles blood request form submissions)
def request_blood(request):
    success_message = ""

    if request.method == "POST":
        patient_name = request.POST.get("requestName")
        blood_type_needed = request.POST.get("requestBloodType")
        hospital_name = request.POST.get("hospital")
        city = request.POST.get("city") 
        phone_number = request.POST.get("phoneNumber")

        if patient_name and blood_type_needed and hospital_name and phone_number:
            BloodRequest.objects.create(
                patient_name=patient_name,
                blood_type_needed=blood_type_needed,
                hospital_name=hospital_name,
                city=city, 
                phone_number=phone_number
            )
            success_message = "✅ Your blood request has been submitted successfully!"

    return render(request, "request-blood.html", {"success_message": success_message})

# Register as a Donor Page (Handles donor registration)
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        blood_type = request.POST.get("blood_type")
        contact_number = request.POST.get("contact_number")
        city = request.POST.get("city")

        if name and blood_type and contact_number and city:
            Donor.objects.create(
                name=name,
                blood_type=blood_type,
                contact_number=contact_number,
                city=city
            )
            messages.success(request, "✅ Registration successful! Thank you for being a donor.")
            return redirect("register")
        else:
            messages.error(request, "All fields are required!")

    return render(request, "register.html")

# View Blood Requests (Visible only to staff/admin after login)
def view_blood_requests(request):
    if request.user.is_authenticated and request.user.is_staff:
        requests = BloodRequest.objects.all()
    else:
        requests = []
    return render(request, 'view_requests.html', {'requests': requests})

# Delete a Blood Request (Only for staff)
@staff_member_required
def delete_blood_request(request, pk):
    req = get_object_or_404(BloodRequest, pk=pk)
    req.delete()
    return redirect('view_blood_requests')

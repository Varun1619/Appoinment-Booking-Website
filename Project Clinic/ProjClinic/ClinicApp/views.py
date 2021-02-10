from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse
from ClinicApp.models import PatientDetails

# Create your views here.

def contact(request):
    if request.method == "POST":
        print("Varun Jhand")
        f_name = request.POST['name_first']
        l_name = request.POST['name_last']
        patient_gender = request.POST['gen']
        age_p = request.POST['age_patient']
        patient_num = request.POST['phone_num']
        patient_issue = request.POST['issue']
        print(f_name, l_name, patient_gender,age_p, patient_num, patient_issue)
        ins = PatientDetails(first_name = f_name, last_name = l_name, gender = patient_gender, patient_age = age_p, phone_number = patient_num, desc = patient_issue)
        ins.save()
        print("Data has been saved")

    return render(request, "contact.html")


def home(request):
    return render(request, "home.html")

def blog(request):
    return render(request,'blog')
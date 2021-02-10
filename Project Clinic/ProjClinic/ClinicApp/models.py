from django.db import models
from twilio.rest import Client
# Create your models here.
class PatientDetails(models.Model):
    first_name = models.CharField(max_length=30, default="default")
    last_name = models.CharField(max_length=30, default="default")
    gender = models.CharField(max_length=30, default="default")
    patient_age = models.CharField(max_length=2, default="default")
    phone_number = models.CharField(max_length=10, default="default")
    desc = models.TextField()
    '''
    def __str__(self):
        return str(self.first_name, self.last_name, self.gender, self.patient_age, self.phone_number, self.desc)
    '''

    def save(self, *args, **kwargs):
        account_sid = "ACca42a1a8cd6177f8b0f9dc51ddadfdd1"
        auth_token = "49d17bb71272527e719c10fcd2a53203"
        client = Client(account_sid, auth_token)
        number_list = ["+919004775788","+919819707659"]
        for i in number_list:
            message = client.messages.create(
                                            body = f"Hello Dr.Nilesh,\n  Patient Name:{self.first_name} {self.last_name}\nGender: {self.gender}\nAge: {self.patient_age}\nPhone : {self.phone_number}\nIssue: {self.desc}",  
                                            from_ = "+19387772398",
                                            to = "+919004775788"
        ) 
        print(message.sid)
        return super().save(*args, **kwargs)
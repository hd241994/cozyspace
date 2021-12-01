from django.db import models
from django.urls import reverse


# Create your models here.

class GetQoute(models.Model):
    #third form
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_number = models.IntegerField() 
    is_number_verified = models.BooleanField(default=False)
    possesion_time = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    reg_date = models.DateTimeField('date published',blank=True, null=True)

    #First Form
    floorPlan = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    
    #Second Form
    kitchen = models.IntegerField(default=0,blank=True, null=True)
    wardrobe = models.IntegerField(default=0,blank=True, null=True)
    crockeryunit = models.IntegerField(default=0,blank=True, null=True)
    poojaroom = models.IntegerField(default=0,blank=True, null=True)
    studyunit = models.IntegerField(default=0,blank=True, null=True)
    entertainmentunit = models.IntegerField(default=0,blank=True, null=True)
    washroom = models.IntegerField(default=0,blank=True, null=True)

    #Renovation Form
    ownertype = models.CharField(max_length=60, blank=True, null=True)
    budget = models.CharField(max_length=60, blank=True, null=True)
    possesion_type = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self) -> str:
        return self.customer_name
    def get_absolute_url(self):
        return f'/customer/{self.id}'

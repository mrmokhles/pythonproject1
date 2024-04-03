from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)




class CountryGDP(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=4)
    year=models.CharField(max_length=5)
    value=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
     return self.name

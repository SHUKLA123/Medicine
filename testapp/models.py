from django.db import models
from django.urls import reverse
class Sell1(models.Model):
    Medicine = models.CharField(max_length = 30)
    Name = models.CharField(max_length = 30)
    Location = models.CharField(max_length = 40)
    Phoneno = models.CharField(max_length = 10)
    quantity = models.IntegerField()
    Email = models.EmailField()
    Pincode = models.IntegerField()
    Batch_No = models.CharField(max_length = 30)
    Total_Amount = models.IntegerField()

class Buy1(models.Model):
    Medicine = models.CharField(max_length = 30)
    Company_Name = models.CharField(max_length = 30)
    Number_of_Tablet = models.IntegerField()
    Location = models.CharField(max_length = 30)
    Email = models.EmailField()
    Pincode = models.IntegerField()
    Phoneno = models.CharField(max_length = 10)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Upload_Prescription(models.Model):
    prescrition = models.FileField(upload_to = 'books/pdfs')

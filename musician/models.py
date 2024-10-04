from django.db import models

class MusicianModel(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email =models.EmailField()
    Phone_number = models.IntegerField()
    Instrument_Type = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.First_Name} {self.Last_name}'
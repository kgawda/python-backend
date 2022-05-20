from django.db import models

class BikeType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    def find_free_bike_for_date(self, date):
        return Bike.objects.filter(biketype=self).exclude(reservation__date=date).first()

class Bike(models.Model):
    name = models.CharField(max_length=100)
    biketype = models.ForeignKey(BikeType, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.biketype.name + ":" + self.name

class Reservation(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    date = models.DateField()
    #client = models.CharField(max_length=100)
    def __str__(self):
        return str(self.bike) + "/" + str(self.date)


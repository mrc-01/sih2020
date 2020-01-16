from django.db import models
from . import utils
# Create your models here.

class accident(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.IntegerField()
    time = models.DateTimeField('Time of accident')
    vehicleinfo = models.TextField()
    deviceinfo = models.TextField()
    # speedometer = models.CharField(max_length=10000, default="")
    
    accelerometerX = models.TextField()
    rotationX = models.TextField()

    accelerometerY = models.TextField()
    rotationY = models.TextField()

    accelerometerZ = models.TextField()
    rotationZ = models.TextField()

    def get_accelerometer_array(self):
        data['x'] =utils.arrayDecode(self.accelerometerX)
        data['y'] =utils.arrayDecode(self.accelerometerY)
        data['z'] =utils.arrayDecode(self.accelerometerZ)

        return data

    def get_rotation_array(self):
        data['x'] =utils.arrayDecode(self.rotationX)
        data['y'] =utils.arrayDecode(self.rotationY)
        data['z'] =utils.arrayDecode(self.rotationZ)

        return data


    def __str__(self):
        return "{}, {}".format(self.uid, self.time)

    class Meta:
        ordering = ["-time"]



class authority(models.Model):

    authority_types = (
        ("hospital", 'Hospital'),
        ("police", 'Police Station'),
        ("fire", 'Fire Station'),
        ("other", 'Other'),
    )

    uid = models.AutoField(primary_key=True)
    authoritytype = models.CharField(max_length=20,choices=authority_types , default="other")
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10 )

    def __str__(self):
        return "{}) {} : {}".format(self.uid, self.authoritytype,self.name)

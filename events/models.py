from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code',max_length=15)
    phone = models.CharField('Contact Phone',max_length=30)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class ClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name 

        
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    venue = models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    event_date = models.DateTimeField('Event Date')
    # venue = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(ClubUser,blank=True)
    register = models.ManyToManyField(ClubUser,related_name="Registered_students")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField('Full Name',max_length=120)
    age = models.IntegerField('Age')
    email = models.EmailField('Email')
    phone = models.IntegerField('Phone Number')
    college = models.CharField('College',max_length=120)
    semester = models.IntegerField('Semester')
    gender = models.CharField('Gender',max_length=20)
    event = models.CharField('Event Name',max_length=120)

    def __str__(self):
        return self.name
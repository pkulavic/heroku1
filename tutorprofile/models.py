from django.db import models

class TutorProfile(models.Model):
    name = models.CharField(max_length=120)
    subject = models.ForeignKey('Subject')
    city = models.ForeignKey('City')
    availability = models.ManyToManyField('Availability')
    bio = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

##################################################

class Subject(models.Model):
    subject = models.CharField(max_length=60)

    def __str__(self):
        return self.subject

##################################################

class City(models.Model):
    city = models.CharField(max_length=60)

    def __str__(self):
        return self.city

##################################################

class Availability(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]
    day = models.CharField(max_length=200, choices=DAY_CHOICES)
    time = models.ForeignKey('Time')

    def __str__(self):
        return "%ss, %s" %(self.day, self.time)

##################################################

class Time(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return "%s - %s" %(self.start_time, self.end_time)

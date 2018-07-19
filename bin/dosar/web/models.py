from django.db import models
#from django import models

class Participants(models.Model):
		name = models.CharField(max_length=30)
		college =models.CharField(max_length=30)
		city = models.CharField(max_length=30)
		accomm = models.CharField(max_length=30)
		events = models.CharField(max_length=30)
		mobile = models.CharField(max_length=11)
		checklist = models.CharField(max_length=10)
		reg_date = models.DateTimeField('date registered')
		fest_id = models.CharField(max_length=15)
		def __unicode__(self):
				return self.name
       

class Sponsors(models.Model):
        name = models.CharField(max_length=30)
        company = models.CharField(max_length=30)
        reg_date = models.DateTimeField('date registered')
        def __unicode__(self):
                return self.name

class Visitors(models.Model):
        name = models.CharField(max_length=30)
        college = models.CharField(max_length=15)
        city = models.CharField(max_length=15)
        mobile = models.CharField(max_length=11)
        purpose = models.CharField(max_length=45)
        fest_id = models.CharField(max_length=15)
        reg_date = models.DateTimeField('date registered')
        def __unicode__(self):
                return self.name
class Special_nights(models.Model):
        college_id  = models.CharField(max_length=14)
        def __unicode__(self):
                return self.college_id

class Spot(models.Model):
        college_id  = models.CharField(max_length=14)
        def __unicode__(self):
                return self.college_id
				
class Entry(models.Model):
        college_id  = models.CharField(max_length=14)
        def __unicode__(self):
                return self.college_id
				
class Vehicle(models.Model):
		name = models.CharField(max_length=30)
		vehicle = models.CharField(max_length=15)
		number = models.CharField(max_length=12)
		mobile = models.CharField(max_length=11)
		deadline = models.CharField(max_length=15)
		def __unicode__(self):
				return self.name
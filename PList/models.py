from django.db import models

'''Gender_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)'''

class Barangay(models.Model):
	Tname = models.TextField(max_length=50, default="")
	birthday = models.CharField(max_length=10, default="")
	gender = models.TextField(max_length=10, default="")
	address = models.CharField(max_length=50, default="")
	cnumber = models.CharField(max_length=11,default=None)
	email = models.CharField(max_length=50, default="")
	usr = models.TextField(max_length=50, default="")
	pas = models.TextField(max_length=50, default="")
	class meta:
		db_table = "vbarangay"

		


class Requirements(models.Model):
	Swabresult_CHOICES = (
  	('Negative', 'negative'),
  	('Positive', 'positive'),)

	Transportations = (
 	('Public', 'public'),
 	('Private', 'private'),)
	
	# Travelprofile = models.(TravelerProfile, on_delete=models.CASCADE)
	Pname = models.TextField(max_length=50, default="")
	swabresult = models.CharField(max_length=50, default=None, choices=Swabresult_CHOICES)
	swabcertificate = models.FileField(upload_to='documents/' ,null=True)
	RidtCard= models.CharField(max_length=100, null=True)
	identificationCards = models.FileField(upload_to='documents/' ,null=True)
	Rtranspo= models.CharField(max_length=100, null=True)
	transportation = models.CharField(max_length=50, default=None, choices=Transportations)
	barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
	class meta:
		db_table = "trequirements"

class Admin(models.Model):
	usrname = models.TextField(max_length=50, default="")
	pasword= models.TextField(max_length=50, default="")


class Certificate(models.Model):
	certificate= models.CharField(max_length=100, null=True)


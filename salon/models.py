from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):

	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name

class ServiceType(models.Model):

	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	description = models.CharField(max_length=128)
	picture = models.ImageField(upload_to='service_images', blank=True)

	def __str__(self):
		return self.name

class Staff(models.Model):

	name = models.CharField(max_length=128, unique=True)
	bio = models.CharField(max_length=128, unique=True)

	class Meta:
		verbose_name_plural = 'Staff'

	def __str__(self):
		return self.name

class Blog(models.Model):
	
	title = models.CharField(max_length=128, unique=True)
	content = models.CharField(max_length=1024)
	publish_date = models.DateField()

	def __str__(self):
		return self.title

class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='profile_images', blank=True)

class Links(models.Model):

	name = models.CharField(max_length=128, unique=True)
	url = models.URLField()
	picture = models.ImageField(upload_to='link_images', blank=True)

	def __str__(self):
		return self.name
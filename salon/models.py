from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceType(models.Model):

	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name

class Service(models.Model):

	service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	description = models.CharField(max_length=128, blank=True)
	picture = models.ImageField(upload_to='service_images', blank=True)

	def __str__(self):
		return self.name


class Staff(models.Model):

	name = models.CharField(max_length=128, unique=True)
	bio = models.CharField(max_length=128, unique=True)
	picture = models.ImageField(upload_to='staff_images/', blank=True)

	class Meta:
		verbose_name_plural = 'Staff'

	def __str__(self):
		return self.name

class Blog(models.Model):
	
	title = models.CharField(max_length=128, unique=True)
	image = models.ImageField(upload_to='blog_images', blank=True)
	content = models.CharField(max_length=1024)
	publish_date = models.DateField()

	def __str__(self):
		return self.title

class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='profile_images', blank=True)

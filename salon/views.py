from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from salon.models import ServiceType, Service, Staff
from salon.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

	template = loader.get_template('salon/index.html')

	service_type_list = ServiceType.objects.all()
	service_types = []

	for serv in service_type_list:
		service_types.append(serv)

	context = {
		'service_types' : service_types, 
	}
	return HttpResponse(template.render(context, request))	

def about(request):

	template = loader.get_template('salon/about.html')

	service_type_list = ServiceType.objects.all()
	service_types = []

	staff_list = Staff.objects.all()
	staff = []

	for serv in service_type_list:
		service_types.append(serv)

	for staff_member in staff_list:
		staff.append(staff_member)

	context = {
		'service_types' : service_types, 
		'staff' : staff,
	}
	return HttpResponse(template.render(context, request))

def services(request, serv_name):

	template = loader.get_template('salon/services.html')
	
	service_type_list = ServiceType.objects.all()
	service_types = []

	for serv in service_type_list:
		service_types.append(serv)

		if serv.name == serv_name:
			service_list = Service.objects.filter(service_type=serv.id)

			print(service_list)

			context = {
				'service_types' : service_types,
				'service_list' : service_list,
				'service_name' : serv.name,
			}

	return HttpResponse(template.render(context, request))

def register(request):
	registered = False
	template = loader.get_template('salon/register.html')

	service_type_list = ServiceType.objects.all()
	service_types = []

	for serv in service_type_list:
		service_types.append(serv)

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True

			return HttpResponseRedirect('/salon/')

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context = {
		'user_form' : user_form,
		'profile_form' : profile_form,
		'registered' : registered,
		'service_types' : service_types,
	}

	return HttpResponse(template.render(context, request))

def user_login(request):
	template = loader.get_template('salon/login.html')

	service_type_list = ServiceType.objects.all()
	service_types = []

	for serv in service_type_list:
		service_types.append(serv)

	context = {
		'service_types' : service_types,
	}

	return HttpResponse(template.render(context, request))
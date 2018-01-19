from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from salon.models import ServiceType, Service, Staff, UserProfile, Blog
from django.contrib.auth.models import User
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

			context = {
				'service_types' : service_types,
				'service_list' : service_list,
				'service_name' : serv.name,
			}

	return HttpResponse(template.render(context, request))

def blog(request):
	template = loader.get_template('salon/blog.html')
	
	service_type_list = ServiceType.objects.all()
	service_types = []

	for serv in service_type_list:
		service_types.append(serv)

	blog_list = Blog.objects.all()
	blogs = []

	for blog in blog_list:
		blogs.append(blog)

	context = {
		'service_types' : service_types, 
		'blogs' : blogs,
	}

	return HttpResponse(template.render(context, request))

def sel_blog(request, blog_name):
	template = loader.get_template('salon/blog.html')
	
	service_type_list = ServiceType.objects.all()
	service_types = []
	context = {}
	active_blog = ''

	for serv in service_type_list:
		service_types.append(serv)

	blog_list = Blog.objects.all()
	blogs = []

	for blog in blog_list:
		blogs.append(blog)

		if blog.title == blog_name:
			active_blog = blog

	context = {
		'service_types' : service_types, 
		'blogs' : blogs,
		'active_blog' : active_blog,
	}

	return HttpResponse(template.render(context, request))	

def search(request):
	template = loader.get_template('salon/search.html')

	service_type_list = ServiceType.objects.all()
	service_types = []

	service_list = Service.objects.all()
	services = []

	for ser in service_list:
		services.append(ser)

	for serv in service_type_list:
		service_types.append(serv)

	result_list = []

	if request.method == 'GET':
		query = request.GET['searchquery']
		
		for ser in services:
			if compare(ser.name, query):
				result_list.append(ser)

	context = {
		'service_types' : service_types, 
		'result_list' : result_list,
	}

	return HttpResponse(template.render(context, request))	

def compare(terma, termb):
	""" 
	Returns true if str terma matches str termb by success_percentage
	"""
	matchlist = []
	success_percentage = 0.5

	for i in terma:
		if i in termb:
			if i not in matchlist:
				matchlist.append(i)
	try:
		if len(matchlist)/len(termb) > success_percentage:
			return True
		else:
			return False
	except ZeroDivisionError:
		return False


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

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		print('STEP 1')

		if user is not None:
			print('STEP 2')

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/salon/')

			else:
				context['user_disabled'] = "Your account has been disabled" 

		else:
			context['invalid_details'] = "Invalid login details"
	
	return HttpResponse(template.render(context, request))

@login_required
def user_page(request, user_name):
	template = loader.get_template('salon/user.html')

	service_type_list = ServiceType.objects.all()
	service_types = []
	service_list = Service.objects.all()

	for serv in service_type_list:
		service_types.append(serv)

	user_profile = UserProfile.objects.all()

	context = {
		'service_types' : service_types,
	}

	for prof in user_profile:
		liked_services = prof.liked_services.all()
		context['liked_services'] = liked_services

		if str(prof.user) == user_name:
			context['profile'] = prof	

			if request.method == 'POST' and 'picture' in request.FILES:
				prof.picture = request.FILES['picture']
				prof.save()

				return HttpResponseRedirect('/salon/user/' + user_name)


	return HttpResponse(template.render(context, request))

@login_required
def user_logout(request):
	logout(request)

	return index(request)

@login_required
def like_service(request):

	service_list = Service.objects.all()
	liked = False

	if request.method == 'GET':
		service_id = int(request.GET['service_id'])
		user_id = int(request.GET['user_id'])
		
		usr = User.objects.get(id=user_id)
		usr_profile = UserProfile.objects.get(user=usr)
		serv = Service.objects.get(id=service_id)
		
		liked = True

	if liked == True:
			
		print(usr_profile.user)

		al = usr_profile.liked_services.all()

		if serv not in al:
			usr_profile.liked_services.add(serv)
			usr_profile.save()
			print("HERE22")

			likes = 1
			ol = serv.likes

			serv.likes = ol + likes
			serv.save()
		
		else:
			dl = usr_profile.liked_services.exclude(name=serv.name)
			usr_profile.liked_services.set(dl)
			usr_profile.save()

			likes = -1
			ol = serv.likes

			serv.likes = ol + likes
			serv.save()
			print("HERE33")

	return user_page(request, serv.name)

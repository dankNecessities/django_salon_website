from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('services/<str:serv_name>', views.services, name='services'),
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login')
]
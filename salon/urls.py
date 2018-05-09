from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('services/<str:serv_name>', views.services, name='services'),
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('user/<str:user_name>', views.user_page, name='user_page'),
	path('likeservice/', views.like_service, name='user_like'),
	path('likeblog/', views.like_blog, name='user_like'),
	path('blog/', views.blog, name='blog'),
	path('blog/<str:blog_name>', views.sel_blog, name='select blog'),
	path('search/', views.search, name='search'),
]
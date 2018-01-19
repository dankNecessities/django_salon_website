from django.contrib import admin
from salon.models import Blog, Staff, UserProfile, ServiceType, Service

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'service_type', 'views', 'likes')

class StaffAdmin(admin.ModelAdmin):
	list_display = ('name', 'bio')

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'publish_date')

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(UserProfile)
admin.site.register(ServiceType)
admin.site.register(Service, ServiceAdmin)
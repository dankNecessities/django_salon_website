from django.contrib import admin
from salon.models import Blog, Staff, UserProfile, ServiceType, Service

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'service_type', 'views', 'likes')

class StaffAdmin(admin.ModelAdmin):
	list_display = ('name', 'bio')

# Register your models here.
admin.site.register(Blog)
admin.site.register(Staff, StaffAdmin)
admin.site.register(UserProfile)
admin.site.register(ServiceType)
admin.site.register(Service, ServiceAdmin)
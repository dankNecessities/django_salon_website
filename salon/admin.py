from django.contrib import admin
from salon.models import Service, ServiceType, Blog, Staff, UserProfile

class ServiceTypeAdmin(admin.ModelAdmin):
	list_display = ('service', 'name', 'views', 'likes')

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Blog)
admin.site.register(Staff)
admin.site.register(UserProfile)

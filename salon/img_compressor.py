from salon.models import Service

service_list = Service.objects.all()

for sv in service_list:
	s_im = sv.picture
	compress_uploaded_image(s_im, (1360, 720))
	sv.picture = s_im
	sv.save()
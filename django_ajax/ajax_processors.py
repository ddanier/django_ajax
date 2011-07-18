def media(request):
	from django.conf import settings
	return {
		'MEDIA_URL': settings.MEDIA_URL
	}

def session(request):
	from django.core.urlresolvers import reverse
	return {
		'session': {
			'authenticated': request.user.is_authenticated(),
			'urls': {
				'login': reverse('ajax_login'),
				'logout': reverse('ajax_logout'),
			}
		}
	}


from django_ajax.config import js_context

def config(request):
	return {
		'JS_CONTEXT': js_context(request)
	}


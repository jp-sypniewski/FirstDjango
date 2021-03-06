from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs are python specific, look these up
	
	return render(request, "home.html", {}) # return request, template name, context (empty dict for now)

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})	

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123, 4242, 12313],
		"my_html": "<h1>Hello world</h1>"
	}
	return render(request, "about.html", my_context)	

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social Page</h1>")
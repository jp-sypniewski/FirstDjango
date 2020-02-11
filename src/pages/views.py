from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs are python specific, look these up
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {}) # return request, template name, context (empty dict for now)
	

def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contact Page</h1>")
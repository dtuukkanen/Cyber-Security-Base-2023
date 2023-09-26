from django.http import HttpResponse
from django.template import loader


# Create your views here.

def homePageView(request):
	return HttpResponse('Home page')

def videoPageView(request):
	return HttpResponse("This is where I'd put my video, if I had any")

from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	content = 'Hello Web!';

		
	return HttpResponse(content)

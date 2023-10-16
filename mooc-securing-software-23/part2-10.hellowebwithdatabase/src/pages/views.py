from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
    # The id of the message is given as a GET parameter id.
    content = 'Hello, Web!'

    if request.method == 'GET':
        id = int(request.GET.get('id'))
        content = Message.objects.get(pk=id).content

    return HttpResponse(content)

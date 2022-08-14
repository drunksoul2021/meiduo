from django.shortcuts import render

# Create your views here.
#view is python function actually

from django.http import HttpRequest
from django.http import HttpResponse
def index(request):

    #return HttpResponse('ok')
    context = {
        'name':'11 is coming'
    }
    return render(request,'book/index.html', context=context)


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def flourimage(request):
    return HttpResponse('yelo flour')

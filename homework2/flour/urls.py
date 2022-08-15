from django.urls import path
from flour.views import flourimage

urlpatterns = [
    path('flourindex',flourimage)
]
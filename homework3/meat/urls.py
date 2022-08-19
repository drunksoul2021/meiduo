from django.urls import path
from meat.views import index


urlpatterns = [
    path('meat/',index)
]
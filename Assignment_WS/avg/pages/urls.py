from django.urls import path
from pages.views import Home, recieve, about

urlpatterns = [
    path('', Home),
    path('recieve/', recieve, name="recieve"),
    path('about/', about),
]
from django.urls import path
from hellow import views

urlpatterns = [
    path('', views.heelloo, name = 'heelloo'),
]
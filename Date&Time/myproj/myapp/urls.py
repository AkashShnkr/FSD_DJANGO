from django.urls import path
from . import views
urlpatterns=[
    path("Time/",views.DateAndTime)
]
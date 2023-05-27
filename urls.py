from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [ 
    path("", views.homepage, name= 'homepage'),
    path("culturalstudies/", views.culture, name = 'culture'),
    path("languagestudies/", views.language, name= 'language'),
    path("contact/", views.contact, name = 'contact'),
    path("indianstudies/", views.indianstudies, name = 'indianstudies'),
    path("arjunmahabharata", views.arjunmahabharata, name= 'arjun'),
    path("spanish/", views.spanish, name= 'spanish'),
    path("stillasapling/", views.stillasapling, name= 'sapling'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("portfolio/", views.portfolio, name="portfolio"),
]
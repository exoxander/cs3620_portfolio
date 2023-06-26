from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("hobbies/<int:item_id>", views.hobbyDetails, name="hobbyDetails"),
    path("portfolio/<int:item_id>", views.portfolioDetails, name="portfolioDetails"),
    path("portfolio/upsert/<int:item_id>", views.upsertItem, name="upsertItem"),
    path("portfolio/delete/<int:item_id>", views.deleteItem, name="deleteItem"),
    path("contact/message", views.message, name="message")
]
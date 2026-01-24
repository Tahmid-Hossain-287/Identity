from django.urls import path

from . import views

urlpatterns = [
    path("links/", views.links, name="links"),
    path("click/<int:link_id>/", views.click_link, name="click_link"),
]
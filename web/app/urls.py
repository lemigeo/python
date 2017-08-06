from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^v1/auth', views.UserController.auth),
    url(r'^v1/user/(?P<idx>[0-9]+)$', views.UserController.user),
]
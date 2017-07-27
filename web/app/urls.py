from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^v1/user/(?P<idx>[0-9]+)$', views.UserController.get),
]
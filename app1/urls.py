from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update-switch-status/", views.update_switch_status, name="update_switch_status"),
    path("alert", views.alert_page, name="alert")
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update-switch-status/", views.update_switch_status, name="update_switch_status"),
    path("auto-update-status/", views.auto_update_status, name="auto_update_status"),
    path("alert", views.alert_page, name="alert"),
    path("graph", views.display_graph, name="graph"),
]
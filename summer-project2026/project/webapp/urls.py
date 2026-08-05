from django.urls import path

from . import views

urlpatterns = [
    path(
        "countdown/",
        views.countdown_widget,
        name="countdown",
    ),
]
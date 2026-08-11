from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name = "webapp/login.html"), name = "login"),

    path("register/", views.register, name="register"),

    path ("", views.home, name = "home"),

    path(
        "countdown/",
        views.countdown_widget,
        name="countdown",
    ),

    path("logout/",auth_views.LogoutView.as_view(), name="logout",),

    path(
        "add-assignment/",
        views.add_assignment,
        name="add_assignment",
),
]
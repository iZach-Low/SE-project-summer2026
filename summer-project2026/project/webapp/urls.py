from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Authentication
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="webapp/login.html"
        ),
        name="login",
    ),

    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # Assignments
    path(
        "add-assignment/",
        views.add_assignment,
        name="add_assignment",
    ),

    path(
        "countdown/",
        views.countdown_widget,
        name="countdown",
    ),

    # Notes
    path(
        "notes/",
        views.notes_list,
        name="notes_list",
    ),

    path(
        "notes/new/",
        views.create_note,
        name="create_note",
    ),

    path(
        "notes/<int:note_id>/edit/",
        views.edit_note,
        name="edit_note",
    ),

    path(
        "notes/<int:note_id>/delete/",
        views.delete_note,
        name="delete_note",
    ),
]
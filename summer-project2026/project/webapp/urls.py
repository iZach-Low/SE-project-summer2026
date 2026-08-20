from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    # Home
    path(
        "",
        views.home,
        name="home",
    ),

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
    # Keep the old URL so any existing links still work.
    path(
        "add-assignment/",
        views.create_assignment,
        name="add_assignment",
    ),

    # New assignment URL used by the countdown page.
    path(
        "assignments/new/",
        views.create_assignment,
        name="create_assignment",
    ),

    path(
    "assignments/<int:assignment_id>/edit/",
    views.edit_assignment,
    name="edit_assignment",
    ),

    path(
    "assignments/<int:assignment_id>/complete/",
    views.complete_assignment,
    name="complete_assignment",
    ),

    path(
    "assignments/<int:assignment_id>/delete/",
    views.delete_assignment,
    name="delete_assignment",
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
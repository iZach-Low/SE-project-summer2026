from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "countdown/",
        views.countdown_widget,
        name="countdown",
    ),

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
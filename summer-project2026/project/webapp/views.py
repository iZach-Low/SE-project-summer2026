from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import NoteForm
from .models import Assignment, Note


# =========================
# Countdown Widget
# =========================

def countdown_widget(request):
    upcoming_assignments = list(
        Assignment.objects.filter(
            done=False,
            due_date__gt=timezone.now(),
        ).order_by("due_date")
    )

    # Start by displaying the three nearest assignments.
    displayed_assignments = upcoming_assignments[:3]

    # If more assignments are due on the same day as the
    # third assignment, display those as well.
    if len(upcoming_assignments) > 3:
        third_assignment = upcoming_assignments[2]

        third_due_date = timezone.localtime(
            third_assignment.due_date
        ).date()

        for assignment in upcoming_assignments[3:]:
            assignment_due_date = timezone.localtime(
                assignment.due_date
            ).date()

            if assignment_due_date == third_due_date:
                displayed_assignments.append(assignment)
            else:
                break

    return render(
        request,
        "webapp/countdown.html",
        {"assignments": displayed_assignments},
    )


# =========================
# Notes List
# =========================

def notes_list(request):
    notes = Note.objects.all().order_by("-updated_at")

    return render(
        request,
        "webapp/notes_list.html",
        {"notes": notes},
    )


# =========================
# Create Note
# =========================

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("notes_list")
    else:
        form = NoteForm()

    return render(
        request,
        "webapp/note_form.html",
        {
            "form": form,
            "page_title": "Create Note",
        },
    )


# =========================
# Edit Note
# =========================

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("notes_list")
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "webapp/note_form.html",
        {
            "form": form,
            "page_title": "Edit Note",
        },
    )


# =========================
# Delete Note
# =========================

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note.delete()

    return redirect("notes_list")

def home(request):
    upcoming_assignments = list(
        Assignment.objects.filter(
            done=False,
            due_date__gt=timezone.now(),
        ).order_by("due_date")
    )

    displayed_assignments = upcoming_assignments[:3]

    if len(upcoming_assignments) > 3:
        third_day = timezone.localtime(
            upcoming_assignments[2].due_date
        ).date()

        for assignment in upcoming_assignments[3:]:
            assignment_day = timezone.localtime(
                assignment.due_date
            ).date()

            if assignment_day == third_day:
                displayed_assignments.append(assignment)
            else:
                break

    recent_notes = Note.objects.all().order_by("-updated_at")[:3]

    return render(
        request,
        "webapp/home.html",
        {
            "assignments": displayed_assignments,
            "notes": recent_notes,
        },
    )
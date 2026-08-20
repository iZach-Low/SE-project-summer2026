from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import AssignmentForm, NoteForm, RegisterForm
from .models import Assignment, Note


# =========================================================
# REGISTER USER
# =========================================================

def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "webapp/register.html",
        {
            "form": form,
        },
    )


# =========================================================
# EDIT ASSIGNMENT
# =========================================================

def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(
        Assignment,
        id=assignment_id,
    )

    if request.method == "POST":
        form = AssignmentForm(
            request.POST,
            instance=assignment,
        )

        if form.is_valid():
            form.save()
            return redirect("countdown")

    else:
        form = AssignmentForm(
            instance=assignment,
        )

    return render(
        request,
        "webapp/assignment_form.html",
        {
            "form": form,
            "page_title": "Edit Assignment",
        },
    )


# =========================================================
# MARK ASSIGNMENT COMPLETE
# =========================================================

def complete_assignment(request, assignment_id):
    assignment = get_object_or_404(
        Assignment,
        id=assignment_id,
    )

    if request.method == "POST":
        assignment.done = True
        assignment.save()

    return redirect("countdown")


# =========================================================
# DELETE ASSIGNMENT
# =========================================================

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(
        Assignment,
        id=assignment_id,
    )

    if request.method == "POST":
        assignment.delete()

    return redirect("countdown")

# =========================================================
# HOME PAGE
# =========================================================

def home(request):
    upcoming_assignments = list(
        Assignment.objects.filter(
            done=False,
            due_date__gt=timezone.now(),
        ).order_by("due_date")
    )

    displayed_assignments = upcoming_assignments[:3]

    # Include additional assignments if they are due
    # on the same day as the third assignment.
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


# =========================================================
# COUNTDOWN PAGE
# =========================================================

def countdown_widget(request):
    upcoming_assignments = list(
        Assignment.objects.filter(
            done=False,
            due_date__gt=timezone.now(),
        ).order_by("due_date")
    )

    displayed_assignments = upcoming_assignments[:3]

    # If more assignments are due on the same day as
    # the third assignment, display those as well.
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
        {
            "assignments": displayed_assignments,
        },
    )


# =========================================================
# CREATE ASSIGNMENT
# =========================================================

def create_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)

        if form.is_valid():
            assignment = form.save(commit=False)

            # New assignments should start as incomplete.
            assignment.done = False

            assignment.save()

            return redirect("countdown")

    else:
        form = AssignmentForm()

    return render(
        request,
        "webapp/assignment_form.html",
        {
            "form": form,
            "page_title": "New Assignment",
        },
    )


# =========================================================
# NOTES LIST
# =========================================================

def notes_list(request):
    notes = Note.objects.all().order_by("-updated_at")

    return render(
        request,
        "webapp/notes_list.html",
        {
            "notes": notes,
        },
    )


# =========================================================
# CREATE NOTE
# =========================================================

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


# =========================================================
# EDIT NOTE
# =========================================================

def edit_note(request, note_id):
    note = get_object_or_404(
        Note,
        id=note_id,
    )

    if request.method == "POST":
        form = NoteForm(
            request.POST,
            instance=note,
        )

        if form.is_valid():
            form.save()

            return redirect("notes_list")

    else:
        form = NoteForm(
            instance=note,
        )

    return render(
        request,
        "webapp/note_form.html",
        {
            "form": form,
            "page_title": "Edit Note",
        },
    )


# =========================================================
# DELETE NOTE
# =========================================================

def delete_note(request, note_id):
    note = get_object_or_404(
        Note,
        id=note_id,
    )

    if request.method == "POST":
        note.delete()

    return redirect("notes_list")
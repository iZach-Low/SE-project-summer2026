from datetime import datetime, time

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Assignment
from .forms import RegisterForm, AssignmentForm


def home(request):
    return redirect("countdown")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("countdown")
    else:
        form = RegisterForm()
    return render(request,"webapp/register.html",
        {"form": form}
     )
@login_required
def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)

        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user
            assignment.save()

            return redirect("countdown")
    else:
        form = AssignmentForm()

    return render(
        request,
        "webapp/add_assignment.html",
        {"form": form}
    )
 
def countdown_widget(request):

    upcoming_assignments = list(
        Assignment.objects.filter(
            user=request.user,
            done=False,
            due_date__gt=timezone.now(),
        ).order_by("due_date")
    )

    displayed_assignments = upcoming_assignments[:3]

    # If there are more than three assignments, include any additional
    # assignments due on the same day as the third assignment.
    if len(upcoming_assignments) > 3:
        third_assignment = upcoming_assignments[2]

        # Convert the deadline into the website's local timezone before
        # comparing dates.
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
                # Assignments are already sorted, so once the date changes,
                # there are no more matching assignments.
                break

    return render(
        request,
        "webapp/countdown.html",
        {"assignments": displayed_assignments},
    )
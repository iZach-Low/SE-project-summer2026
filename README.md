# SE-project-summer2026

Team:
- AlejandroBenavides02
- PeterEMoreno
- iZach-Low (isaac lopez)

# Assignment Reminder

A web application that helps students keep track of assignment deadlines. Students add their assignments with due dates, and the app displays a live countdown showing exactly how much time remains before each one is due — so instead of digging through a planner or learning-management system, you can glance at one dashboard and see what needs attention next.

## Features

- **User accounts** — register, log in, and log out. Each student sees only their own assignments.
- **Assignment tracking** — add assignments with a title, class name, due date/time, and completion status.
- **Live countdown** — each assignment shows a real-time countdown (days/hours/minutes/seconds) that updates every second, color-coded by urgency (red under 24 hours, yellow under 72 hours, green beyond that).
- **Upcoming focus** — the dashboard highlights the nearest deadlines; past-due assignments are filtered out of the upcoming view.
- **Class notes** — a built-in notes section where students can keep notes for each class in one place.

## Tech Stack

- **Backend:** Django 6.0 (Python)
- **Frontend:** Django templates with Bootstrap 5, styled with a custom "library" theme via template inheritance
- **Database:** SQLite (development)

## Getting Started

### Prerequisites
- Python 3.12+
- pip

### Setup

1. Clone the repository:
git clone https://github.com/iZach-Low/SE-project-summer2026.git
cd SE-project-summer2026/summer-project2026

2. Create and activate a virtual environment:
python3 -m venv virt
source virt/bin/activate # On Windows: virt\Scripts\activate

3. Install dependencies:
pip install -r ../requirements.txt

4. Move into the project folder (where `manage.py` lives) and set up the database:
cd project
python manage.py migrate

5. Create an admin account (optional, for the Django admin page):
python manage.py createsuperuser

6. Run the development server:
python manage.py runserver

7. Open your browser to `http://127.0.0.1:8000/`

from flask import Blueprint

# Module: Tasks + Communication
# Covers: tasks, follow-ups, reminders, notes/activity timeline
bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("/")
def list_tasks():
    return "Task list placeholder"

from flask import Blueprint

# Module: Deals + Sales Pipeline
# Covers: deals, deal values, stages, Kanban pipeline, won/lost, revenue calculations
bp = Blueprint("deals", __name__, url_prefix="/deals")


@bp.route("/")
def list_deals():
    return "Deals pipeline placeholder"

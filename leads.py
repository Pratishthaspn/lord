from flask import Blueprint

# Module: Lead Management
# Covers: lead CRUD, status, source, assignment, search/filtering, convert to customer
bp = Blueprint("leads", __name__, url_prefix="/leads")


@bp.route("/")
def list_leads():
    return "Lead list placeholder"

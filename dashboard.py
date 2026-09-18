from flask import Blueprint

# Module: Dashboard + Analytics + Integration
# Covers: dashboard UI, charts, KPIs, revenue/customer/lead stats, notifications
bp = Blueprint("dashboard", __name__, url_prefix="/")


@bp.route("/")
def home():
    return "Dashboard placeholder"

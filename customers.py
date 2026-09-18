from flask import Blueprint

# Module: Customer Management
# Covers: customer CRUD, profiles, search/filtering, tags/categories
bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.route("/")
def list_customers():
    return "Customer list placeholder"

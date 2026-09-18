from flask import Blueprint, render_template

# Module: Authentication + Users
# Covers: login/signup, logout, forgot password, user profiles, roles/admin access
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return "Login page placeholder"


@bp.route("/signup")
def signup():
    return "Signup page placeholder"

from datetime import datetime
from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="user")  # "admin" or "user"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    company = db.Column(db.String(120))
    tags = db.Column(db.String(200))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    status = db.Column(db.String(30), default="new")  # new/contacted/qualified/lost
    source = db.Column(db.String(80))
    assigned_to = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    value = db.Column(db.Float, default=0.0)
    stage = db.Column(db.String(30), default="lead")  # lead/contacted/proposal/won/lost
    expected_close_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=True)
    lead_id = db.Column(db.Integer, db.ForeignKey("lead.id"), nullable=True)
    deal_id = db.Column(db.Integer, db.ForeignKey("deal.id"), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(30), default="note")  # call/email/meeting/note
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=True)
    lead_id = db.Column(db.Integer, db.ForeignKey("lead.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

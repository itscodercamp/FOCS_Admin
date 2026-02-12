from datetime import datetime
from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

class ContactQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(50))
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class PartnershipRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_role = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    resume_link = db.Column(db.String(255))
    cover_letter = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    student_name = db.Column(db.String(100), nullable=False)
    college = db.Column(db.String(150))
    year = db.Column(db.String(20))
    description = db.Column(db.Text)  # Short summary for card
    full_description = db.Column(db.Text)  # Detailed description
    duration = db.Column(db.String(50))
    tech_stack = db.Column(db.Text)  # Stored as comma-separated string
    thumbnail = db.Column(db.String(255))
    screenshots = db.Column(db.Text)  # Stored as comma-separated URLs
    live_link = db.Column(db.String(255))
    repo_link = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50))  # Workshop, Seminar, etc.
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    venue = db.Column(db.String(150))
    organizer = db.Column(db.String(100))
    short_desc = db.Column(db.Text)
    full_desc = db.Column(db.Text)
    main_image = db.Column(db.String(255))
    gallery = db.Column(db.Text)  # Stored as comma-separated URLs
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

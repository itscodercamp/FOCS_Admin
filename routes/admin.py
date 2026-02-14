import os
import re
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from extensions import db
from models import User, ContactQuery, PartnershipRequest, JobApplication, Project, Event, Vacancy

admin_bp = Blueprint('admin', __name__)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text

def save_file(file, folder):
    if not file or file.filename == '':
        return None
    filename = secure_filename(file.filename)
    # Add timestamp prefix to avoid collisions
    from datetime import datetime
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], folder)
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))
    # Return as relative path for web access: /static/uploads/...
    return f"/static/uploads/{folder}/{filename}"


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    contact_queries = ContactQuery.query.order_by(ContactQuery.timestamp.desc()).all()
    partnership_requests = PartnershipRequest.query.order_by(PartnershipRequest.timestamp.desc()).all()
    job_applications = JobApplication.query.order_by(JobApplication.timestamp.desc()).all()
    projects_count = Project.query.count()
    events_count = Event.query.count()
    
    return render_template('admin/dashboard.html', 
                         contact_queries=contact_queries,
                         partnership_requests=partnership_requests,
                         job_applications=job_applications,
                         projects_count=projects_count,
                         events_count=events_count)

# --- Contact Routes ---
@admin_bp.route('/contacts')
@login_required
def contacts():
    contact_queries = ContactQuery.query.order_by(ContactQuery.timestamp.desc()).all()
    return render_template('admin/contacts.html', contact_queries=contact_queries)

@admin_bp.route('/contacts/delete/<int:id>', methods=['POST'])
@login_required
def delete_contact(id):
    query = ContactQuery.query.get_or_404(id)
    db.session.delete(query)
    db.session.commit()
    flash('Contact query deleted successfully.', 'success')
    return redirect(url_for('admin.contacts'))

@admin_bp.route('/contacts/view/<int:id>')
@login_required
def view_contact(id):
    contact = ContactQuery.query.get_or_404(id)
    return render_template('admin/view_contact.html', contact=contact)

# --- Partnership Routes ---
@admin_bp.route('/partnerships')
@login_required
def partnerships():
    partnership_requests = PartnershipRequest.query.order_by(PartnershipRequest.timestamp.desc()).all()
    return render_template('admin/partnerships.html', partnership_requests=partnership_requests)

@admin_bp.route('/partnerships/delete/<int:id>', methods=['POST'])
@login_required
def delete_partnership(id):
    req = PartnershipRequest.query.get_or_404(id)
    db.session.delete(req)
    db.session.commit()
    flash('Partnership request deleted successfully.', 'success')
    return redirect(url_for('admin.partnerships'))

@admin_bp.route('/partnerships/view/<int:id>')
@login_required
def view_partnership(id):
    req = PartnershipRequest.query.get_or_404(id)
    return render_template('admin/view_partnership.html', req=req)

# --- Careers Routes ---
@admin_bp.route('/careers')
@login_required
def careers():
    job_applications = JobApplication.query.order_by(JobApplication.timestamp.desc()).all()
    return render_template('admin/careers.html', job_applications=job_applications)

@admin_bp.route('/careers/delete/<int:id>', methods=['POST'])
@login_required
def delete_career(id):
    app = JobApplication.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()
    flash('Job application deleted successfully.', 'success')
    return redirect(url_for('admin.careers'))

@admin_bp.route('/careers/view/<int:id>')
@login_required
def view_career(id):
    app = JobApplication.query.get_or_404(id)
    return render_template('admin/view_career.html', app=app)

# --- Vacancies Routes ---
@admin_bp.route('/vacancies')
@login_required
def vacancies():
    all_vacancies = Vacancy.query.order_by(Vacancy.timestamp.desc()).all()
    return render_template('admin/vacancies.html', vacancies=all_vacancies)

@admin_bp.route('/vacancies/add', methods=['GET', 'POST'])
@login_required
def add_vacancy():
    if request.method == 'POST':
        try:
            title = request.form.get('title')
            slug = slugify(title)
            # Ensure unique slug
            existing = Vacancy.query.filter_by(slug=slug).first()
            if existing:
                import random
                slug = f"{slug}-{random.randint(100, 999)}"

            new_vacancy = Vacancy(
                title=title,
                slug=slug,
                location=request.form.get('location'),
                type=request.form.get('type'),
                description=request.form.get('description'),
                requirements=request.form.get('requirements'),
                is_active=True
            )
            db.session.add(new_vacancy)
            db.session.commit()
            flash('Job vacancy added successfully!', 'success')
            return redirect(url_for('admin.vacancies'))
        except Exception as e:
            flash(f'Error adding vacancy: {str(e)}', 'danger')
    
    return render_template('admin/add_vacancy.html')

@admin_bp.route('/vacancies/delete/<int:id>', methods=['POST'])
@login_required
def delete_vacancy(id):
    vacancy = Vacancy.query.get_or_404(id)
    db.session.delete(vacancy)
    db.session.commit()
    flash('Job vacancy deleted successfully.', 'success')
    return redirect(url_for('admin.vacancies'))

@admin_bp.route('/vacancies/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_vacancy(id):
    vacancy = Vacancy.query.get_or_404(id)
    if request.method == 'POST':
        try:
            vacancy.title = request.form.get('title')
            vacancy.location = request.form.get('location')
            vacancy.type = request.form.get('type')
            vacancy.description = request.form.get('description')
            vacancy.requirements = request.form.get('requirements')
            
            db.session.commit()
            flash('Vacancy updated successfully!', 'success')
            return redirect(url_for('admin.vacancies'))
        except Exception as e:
            flash(f'Error updating vacancy: {str(e)}', 'danger')
            
    return render_template('admin/edit_vacancy.html', vacancy=vacancy)

@admin_bp.route('/vacancies/view/<int:id>')
@login_required
def view_vacancy(id):
    vacancy = Vacancy.query.get_or_404(id)
    return render_template('admin/view_vacancy.html', vacancy=vacancy)

# --- Projects Routes ---
@admin_bp.route('/projects')
@login_required
def projects():
    all_projects = Project.query.order_by(Project.timestamp.desc()).all()
    return render_template('admin/projects.html', projects=all_projects)

@admin_bp.route('/projects/add', methods=['GET', 'POST'])
@login_required
def add_project():
    if request.method == 'POST':
        try:
            title = request.form.get('title')
            full_description = request.form.get('full_description', '')
            
            # Auto-generate slug
            slug = slugify(title)
            # Ensure unique slug
            existing = Project.query.filter_by(slug=slug).first()
            if existing:
                import random
                slug = f"{slug}-{random.randint(100, 999)}"

            # Auto-generate short description from full description (first 150 chars)
            description = full_description[:150] + ('...' if len(full_description) > 150 else '')

            # Handle file uploads
            thumbnail_file = request.files.get('thumbnail')
            thumbnail_path = save_file(thumbnail_file, 'projects')

            screenshot_files = request.files.getlist('screenshots')
            screenshot_paths = []
            for f in screenshot_files:
                path = save_file(f, 'projects/screenshots')
                if path:
                    screenshot_paths.append(path)
            
            tech_stack = request.form.get('tech_stack', '')
            
            new_project = Project(
                title=title,
                slug=slug,
                student_name=request.form.get('student_name'),
                college=request.form.get('college'),
                year=request.form.get('year'),
                description=description,
                full_description=full_description,
                duration=request.form.get('duration'),
                tech_stack=tech_stack,
                thumbnail=thumbnail_path,
                screenshots=','.join(screenshot_paths),
                live_link=request.form.get('live_link'),
                repo_link=request.form.get('repo_link')
            )
            db.session.add(new_project)
            db.session.commit()
            flash('Project added successfully!', 'success')
            return redirect(url_for('admin.projects'))
        except Exception as e:
            flash(f'Error adding project: {str(e)}', 'danger')
    
    return render_template('admin/add_project.html')

@admin_bp.route('/projects/delete/<int:id>', methods=['POST'])
@login_required
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully.', 'success')
    return redirect(url_for('admin.projects'))

@admin_bp.route('/projects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.method == 'POST':
        try:
            project.title = request.form.get('title')
            project.student_name = request.form.get('student_name')
            project.college = request.form.get('college')
            project.year = request.form.get('year')
            project.full_description = request.form.get('full_description')
            project.description = project.full_description[:150] + '...' if len(project.full_description) > 150 else project.full_description
            project.duration = request.form.get('duration')
            project.tech_stack = request.form.get('tech_stack')
            project.live_link = request.form.get('live_link')
            project.repo_link = request.form.get('repo_link')

            # Handle file uploads
            thumbnail_file = request.files.get('thumbnail')
            if thumbnail_file and thumbnail_file.filename:
                project.thumbnail = save_file(thumbnail_file, 'projects')

            screenshot_files = request.files.getlist('screenshots')
            new_screenshots = []
            for f in screenshot_files:
                path = save_file(f, 'projects/screenshots')
                if path:
                    new_screenshots.append(path)
            
            if new_screenshots:
                current = project.screenshots.split(',') if project.screenshots else []
                project.screenshots = ','.join(current + new_screenshots)
            
            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('admin.projects'))
        except Exception as e:
            flash(f'Error updating project: {str(e)}', 'danger')
            
    return render_template('admin/edit_project.html', project=project)

@admin_bp.route('/projects/view/<int:id>')
@login_required
def view_project(id):
    project = Project.query.get_or_404(id)
    return render_template('admin/view_project.html', project=project)

# --- Events Routes ---
@admin_bp.route('/events')
@login_required
def events():
    all_events = Event.query.order_by(Event.timestamp.desc()).all()
    return render_template('admin/events.html', events=all_events)

@admin_bp.route('/events/add', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':
        try:
            title = request.form.get('title')
            full_desc = request.form.get('full_desc', '')
            
            # Auto-generate slug
            slug = slugify(title)
            # Ensure unique slug
            existing = Event.query.filter_by(slug=slug).first()
            if existing:
                import random
                slug = f"{slug}-{random.randint(100, 999)}"

            # Auto-generate short description from full description (first 150 chars)
            short_desc = full_desc[:150] + ('...' if len(full_desc) > 150 else '')

            # Category handling
            category = request.form.get('category')
            if category == 'Other':
                category = request.form.get('custom_category')

            # Handle file uploads
            main_image_file = request.files.get('main_image')
            main_image_path = save_file(main_image_file, 'events')

            gallery_files = request.files.getlist('gallery')
            gallery_paths = []
            for f in gallery_files:
                path = save_file(f, 'events/gallery')
                if path:
                    gallery_paths.append(path)
            
            new_event = Event(
                title=title,
                slug=slug,
                category=category,
                date=request.form.get('date'),
                time=request.form.get('time'),
                venue=request.form.get('venue'),
                organizer=request.form.get('organizer'),
                short_desc=short_desc,
                full_desc=full_desc,
                main_image=main_image_path,
                gallery=','.join(gallery_paths)
            )
            db.session.add(new_event)
            db.session.commit()
            flash('Event added successfully!', 'success')
            return redirect(url_for('admin.events'))
        except Exception as e:
            flash(f'Error adding event: {str(e)}', 'danger')
    
    return render_template('admin/add_event.html')

@admin_bp.route('/events/delete/<int:id>', methods=['POST'])
@login_required
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully.', 'success')
    return redirect(url_for('admin.events'))

@admin_bp.route('/events/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    event = Event.query.get_or_404(id)
    if request.method == 'POST':
        try:
            event.title = request.form.get('title')
            event.full_desc = request.form.get('full_desc')
            event.short_desc = event.full_desc[:150] + '...' if len(event.full_desc) > 150 else event.full_desc
            
            category = request.form.get('category')
            if category == 'Other':
                category = request.form.get('custom_category')
            event.category = category
            
            event.date = request.form.get('date')
            event.time = request.form.get('time')
            event.venue = request.form.get('venue')
            event.organizer = request.form.get('organizer')
            
            # Handle images
            main_image_file = request.files.get('main_image')
            if main_image_file and main_image_file.filename:
                event.main_image = save_file(main_image_file, 'events')

            # Append new gallery images
            gallery_files = request.files.getlist('gallery')
            new_gallery = []
            for f in gallery_files:
                path = save_file(f, 'events/gallery')
                if path:
                    new_gallery.append(path)
            
            if new_gallery:
                current_gallery = event.gallery.split(',') if event.gallery else []
                event.gallery = ','.join(current_gallery + new_gallery)
            
            db.session.commit()
            flash('Event updated successfully!', 'success')
            return redirect(url_for('admin.events'))
        except Exception as e:
            flash(f'Error updating event: {str(e)}', 'danger')

    return render_template('admin/edit_event.html', event=event)

@admin_bp.route('/events/view/<int:id>')
@login_required
def view_event(id):
    event = Event.query.get_or_404(id)
    return render_template('admin/view_event.html', event=event)

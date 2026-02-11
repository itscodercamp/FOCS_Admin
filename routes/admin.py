from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from extensions import db
from models import User, ContactQuery, PartnershipRequest, JobApplication

admin_bp = Blueprint('admin', __name__)

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
    
    return render_template('admin/dashboard.html', 
                         contact_queries=contact_queries,
                         partnership_requests=partnership_requests,
                         job_applications=job_applications)

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

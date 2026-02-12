from flask import Blueprint, request, jsonify
from extensions import db
from models import ContactQuery, PartnershipRequest, JobApplication, Project, Event, Vacancy

api_bp = Blueprint('api', __name__)

@api_bp.route('/vacancies', methods=['GET'])
def get_vacancies():
    """Get all active job vacancies for frontend"""
    try:
        vacancies = Vacancy.query.filter_by(is_active=True).order_by(Vacancy.timestamp.desc()).all()
        vacancies_list = []
        
        for v in vacancies:
            vacancies_list.append({
                'id': v.id,
                'title': v.title,
                'slug': v.slug,
                'location': v.location,
                'type': v.type,
                'description': v.description,
                'requirements': v.requirements.split(',') if v.requirements else [],
                'timestamp': v.timestamp.isoformat() if v.timestamp else None
            })
        
        return jsonify(vacancies_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        new_query = ContactQuery(
            name=data.get('name'),
            email=data.get('email'),
            type=data.get('type'),
            message=data.get('message')
        )
        db.session.add(new_query)
        db.session.commit()
        return jsonify({'message': 'Contact query submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/academy/partnership', methods=['POST'])
def partnership():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        new_partnership = PartnershipRequest(
            college_name=data.get('collegeName'),
            email=data.get('email'),
            phone=data.get('phone')
        )
        db.session.add(new_partnership)
        db.session.commit()
        return jsonify({'message': 'Partnership request submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/careers/apply', methods=['POST'])
def careers():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        new_application = JobApplication(
            job_role=data.get('jobRole'),
            name=data.get('name'),
            email=data.get('email'),
            resume_link=data.get('resumeLink'),
            cover_letter=data.get('coverLetter')
        )
        db.session.add(new_application)
        db.session.commit()
        return jsonify({'message': 'Job application submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============ PROJECTS API ============

@api_bp.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects for frontend showcase"""
    try:
        projects = Project.query.order_by(Project.timestamp.desc()).all()
        projects_list = []
        
        for project in projects:
            projects_list.append({
                'id': project.id,
                'title': project.title,
                'slug': project.slug,
                'studentName': project.student_name,
                'college': project.college,
                'year': project.year,
                'description': project.description,
                'fullDescription': project.full_description,
                'duration': project.duration,
                'techStack': project.tech_stack.split(',') if project.tech_stack else [],
                'thumbnail': project.thumbnail,
                'screenshots': project.screenshots.split(',') if project.screenshots else [],
                'liveLink': project.live_link,
                'repoLink': project.repo_link,
                'timestamp': project.timestamp.isoformat() if project.timestamp else None
            })
        
        return jsonify(projects_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/projects', methods=['POST'])
def add_project():
    """Add new project (Admin use)"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Convert arrays to comma-separated strings
        tech_stack_str = ','.join(data.get('techStack', []))
        screenshots_str = ','.join(data.get('screenshots', []))
        
        new_project = Project(
            title=data.get('title'),
            student_name=data.get('studentName'),
            college=data.get('college'),
            year=data.get('year'),
            description=data.get('description'),
            full_description=data.get('fullDescription'),
            duration=data.get('duration'),
            tech_stack=tech_stack_str,
            thumbnail=data.get('thumbnail'),
            screenshots=screenshots_str,
            live_link=data.get('liveLink'),
            repo_link=data.get('repoLink')
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully', 'id': new_project.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ============ EVENTS API ============

@api_bp.route('/events', methods=['GET'])
def get_events():
    """Get all events for frontend"""
    try:
        events = Event.query.order_by(Event.timestamp.desc()).all()
        events_list = []
        
        for event in events:
            events_list.append({
                'id': event.id,
                'title': event.title,
                'slug': event.slug,
                'category': event.category,
                'date': event.date,
                'time': event.time,
                'venue': event.venue,
                'organizer': event.organizer,
                'shortDesc': event.short_desc,
                'fullDesc': event.full_desc,
                'mainImage': event.main_image,
                'gallery': event.gallery.split(',') if event.gallery else [],
                'timestamp': event.timestamp.isoformat() if event.timestamp else None
            })
        
        return jsonify(events_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/events', methods=['POST'])
def add_event():
    """Add new event (Admin use)"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Convert gallery array to comma-separated string
        gallery_str = ','.join(data.get('gallery', []))
        
        new_event = Event(
            title=data.get('title'),
            category=data.get('category'),
            date=data.get('date'),
            time=data.get('time'),
            venue=data.get('venue'),
            organizer=data.get('organizer'),
            short_desc=data.get('shortDesc'),
            full_desc=data.get('fullDesc'),
            main_image=data.get('mainImage'),
            gallery=gallery_str
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event added successfully', 'id': new_event.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

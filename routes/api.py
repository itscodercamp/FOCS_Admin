from flask import Blueprint, request, jsonify
from extensions import db
from models import ContactQuery, PartnershipRequest, JobApplication

api_bp = Blueprint('api', __name__)

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

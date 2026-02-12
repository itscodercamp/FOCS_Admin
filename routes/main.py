from flask import Blueprint, redirect, url_for, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('public/index.html')

@main_bp.route('/test-api')
def test_api():
    return render_template('public/api_test.html')

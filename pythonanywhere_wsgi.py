# This file contains the WSGI configuration required to serve up your
# web application at http://Steve5911.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

import sys
import os

# add your project directory to the sys.path
project_home = '/home/Steve5911/AI_Labs_Portal'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables (Recommended for production)
# os.environ['SECRET_KEY'] = 'your-secret-key'
# os.environ['DATABASE_URL'] = 'sqlite:////home/Steve5911/AI_Labs_Portal/instance/database.db'

# Import the application factory
from app import create_app

# Create the application instance
# PythonAnywhere looks for a variable named 'application'
application = create_app()

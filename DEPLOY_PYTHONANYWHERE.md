# Deploying to PythonAnywhere

Follow these steps to deploy your AI Labs Admin Panel to PythonAnywhere for live testing.

## 1. Prepare Your Code
1.  **Zip the Project**: Select all files in your `AI_Labs_Portal` folder and zip them (e.g., `portal.zip`).
    *   *Exclude `venv` and `__pycache__` folders to save space.*

## 2. Upload to PythonAnywhere
1.  Log in to your [PythonAnywhere Dashboard](https://www.pythonanywhere.com/).
2.  Go to the **Files** tab.
3.  Upload `portal.zip` to `/home/yourusername/`.
4.  Open a **Bash Console** (from Dashboard).
5.  Unzip the file:
    ```bash
    unzip portal.zip -d mysite
    ```

## 3. Set Up Virtual Environment
In the Bash Console, run:
```bash
cd mysite
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```
*(Note: `mkvirtualenv` might not work in some layouts. If not, use `python3 -m venv myenv` and activate it).*

## 4. Configure Web App
1.  Go to the **Web** tab.
2.  **Add a new web app** -> **Manual Configuration** -> **Python 3.10**.
3.  **Virtualenv**: Enter the path to your virtualenv (e.g., `/home/yourusername/.virtualenvs/myenv` or `/home/yourusername/mysite/myenv`).

## 5. Configure WSGI File
1.  In the **Web** tab, click the link to edit the **WSGI configuration file** (it looks like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
2.  Delete everything and paste this:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables (Optional but recommended)
os.environ['SECRET_KEY'] = 'your-secret-key-here'

# Import flask app but need to call create_app
from app import create_app
application = create_app()
```
*Replace `yourusername` with your actual PythonAnywhere username.*

## 6. Finish
1.  Go back to the **Web** tab and click **Reload**.
2.  Open your site URL (e.g., `yourusername.pythonanywhere.com`).
3.  It should redirect to `/admin/login`.
4.  **Login**: `admin` / `admin123`.

## Troubleshooting
- If you see "Something went wrong", check the **Error Log** link in the Web tab.
- If images/CSS are missing, go to **Web Tab -> Static Files**:
    - URL: `/static/`
    - Directory: `/home/yourusername/mysite/static`

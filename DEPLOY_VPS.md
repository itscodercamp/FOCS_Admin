# AI Labs Portal - VPS/KVM Deployment Guide

Complete deployment guide for deploying the AI Labs Admin Panel on a VPS/KVM server using **Gunicorn** and **Nginx**.

---

## 🖥️ Server Requirements

- **OS**: Ubuntu 20.04+ / Debian 11+
- **Python**: 3.8+
- **RAM**: 512MB minimum (1GB recommended)
- **Storage**: 5GB
- **Ports**: 80 (HTTP), 443 (HTTPS optional)

---

## 📦 Step 1: Server Setup

### 1.1. Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2. Install Required Packages
```bash
sudo apt install python3 python3-pip python3-venv nginx git -y
```

---

## 🚀 Step 2: Deploy Application

### 2.1. Clone Repository
```bash
cd /var/www
sudo git clone https://github.com/itscodercamp/FOCS_Admin.git AI_Labs_Portal
cd AI_Labs_Portal
```

### 2.2. Set Permissions
```bash
sudo chown -R www-data:www-data /var/www/AI_Labs_Portal
```

### 2.3. Create Virtual Environment
```bash
sudo -u www-data python3 -m venv venv
sudo -u www-data venv/bin/pip install -r requirements.txt
```

### 2.4. Set Environment Variables (Optional but Recommended)
```bash
sudo nano /var/www/AI_Labs_Portal/.env
```

Add the following:
```env
SECRET_KEY=your-super-secret-key-here-change-this
FLASK_DEBUG=false
PORT=8000
```

---

## ⚙️ Step 3: Configure Gunicorn Service

### 3.1. Copy Service File
```bash
sudo cp ai_labs.service /etc/systemd/system/
```

### 3.2. Enable and Start Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable ai_labs
sudo systemctl start ai_labs
```

### 3.3. Check Status
```bash
sudo systemctl status ai_labs
```

**Expected Output:**
```
● ai_labs.service - AI Labs Admin Panel - Gunicorn Application
   Loaded: loaded (/etc/systemd/system/ai_labs.service; enabled)
   Active: active (running)
```

---

## 🌐 Step 4: Configure Nginx

### 4.1. Create Nginx Config
```bash
sudo nano /etc/nginx/sites-available/ai_labs
```

**Paste this configuration:**
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;  # Change this

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /var/www/AI_Labs_Portal/static/;
        expires 30d;
    }
}
```

### 4.2. Enable Site
```bash
sudo ln -s /etc/nginx/sites-available/ai_labs /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl restart nginx
```

---

## 🔒 Step 5: SSL Certificate (Optional but Recommended)

### 5.1. Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 5.2. Get SSL Certificate
```bash
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

Follow the prompts. Certbot will automatically configure HTTPS.

---

## 📊 Step 6: Verify Deployment

1. **Access Admin Panel**: `http://your-domain.com/admin/login`
2. **Login**: `admin` / `admin123`
3. **Test API**: 
   ```bash
   curl http://your-domain.com/api/projects
   ```

---

## 🔧 Management Commands

### Check Application Logs
```bash
sudo journalctl -u ai_labs -f
```

### Restart Application
```bash
sudo systemctl restart ai_labs
```

### Stop Application
```bash
sudo systemctl stop ai_labs
```

### Update Application
```bash
cd /var/www/AI_Labs_Portal
sudo -u www-data git pull
sudo systemctl restart ai_labs
```

---

## 🛡️ Security Best Practices

### 1. Change Default Admin Password
```bash
# Use Flask shell to update password
cd /var/www/AI_Labs_Portal
sudo -u www-data venv/bin/python
>>> from app import create_app
>>> from extensions import db
>>> from models import User
>>> from werkzeug.security import generate_password_hash
>>> app = create_app()
>>> with app.app_context():
...     admin = User.query.filter_by(username='admin').first()
...     admin.password_hash = generate_password_hash('your-new-password')
...     db.session.commit()
>>> exit()
```

### 2. Set Strong SECRET_KEY
Edit `/var/www/AI_Labs_Portal/.env` and add:
```env
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
```

### 3. Configure Firewall
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp  # SSH
sudo ufw enable
```

---

## 🐛 Troubleshooting

### Application Not Starting
```bash
# Check logs
sudo journalctl -u ai_labs -n 50

# Check if port is in use
sudo netstat -tlnp | grep 8000

# Verify permissions
ls -la /var/www/AI_Labs_Portal
```

### Nginx Errors
```bash
# Check Nginx logs
sudo tail -f /var/log/nginx/error.log

# Test configuration
sudo nginx -t
```

### Database Issues
```bash
# Recreate database
cd /var/www/AI_Labs_Portal
sudo -u www-data venv/bin/python
>>> from app import create_app
>>> from extensions import db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

---

## 📈 Performance Optimization

### Increase Gunicorn Workers
Edit `/etc/systemd/system/ai_labs.service`:
```ini
ExecStart=/var/www/AI_Labs_Portal/venv/bin/gunicorn --workers 5 --bind 0.0.0.0:8000 'app:create_app()'
```
Then:
```bash
sudo systemctl daemon-reload
sudo systemctl restart ai_labs
```

### Enable Gzip Compression in Nginx
Add to `/etc/nginx/sites-available/ai_labs`:
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript;
```

---

## 🔄 Auto-Restart on Failure

The systemd service automatically restarts on failure. To customize:

```bash
sudo nano /etc/systemd/system/ai_labs.service
```

Add under `[Service]`:
```ini
Restart=always
RestartSec=3
```

---

## 📞 Support

- **GitHub**: https://github.com/itscodercamp/FOCS_Admin
- **Admin Panel**: `http://your-domain.com/admin/login`
- **API Docs**: See `API_DOCUMENTATION.md`

---

## ✅ Quick Deployment Commands Summary

```bash
# 1. Install dependencies
sudo apt update && sudo apt install python3 python3-pip python3-venv nginx git -y

# 2. Clone and setup
cd /var/www
sudo git clone https://github.com/itscodercamp/FOCS_Admin.git AI_Labs_Portal
cd AI_Labs_Portal
sudo chown -R www-data:www-data .
sudo -u www-data python3 -m venv venv
sudo -u www-data venv/bin/pip install -r requirements.txt

# 3. Configure service
sudo cp ai_labs.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ai_labs
sudo systemctl start ai_labs

# 4. Configure Nginx (create config as shown above)
sudo nano /etc/nginx/sites-available/ai_labs
sudo ln -s /etc/nginx/sites-available/ai_labs /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# 5. Done! Access at http://your-domain.com
```

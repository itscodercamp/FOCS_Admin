# AI Labs Portal - Custom VPS Deployment
# Path: /root/FOCS_STUFFS

## 🚀 Complete Deployment Guide for /root/FOCS_STUFFS

---

## Step 1: Initial Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install python3 python3-pip python3-venv nginx git -y
```

---

## Step 2: Clone and Setup Application

```bash
# Create directory and clone
cd /root
mkdir -p FOCS_STUFFS
cd FOCS_STUFFS
git clone https://github.com/itscodercamp/FOCS_Admin.git
cd FOCS_Admin

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate (optional)
deactivate
```

---

## Step 3: Create Systemd Service

```bash
# Create service file
sudo nano /etc/systemd/system/ai_labs.service
```

**Paste this content:**

```ini
[Unit]
Description=AI Labs Admin Panel - Gunicorn Application
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/root/FOCS_STUFFS/FOCS_Admin
Environment="PATH=/root/FOCS_STUFFS/FOCS_Admin/venv/bin"
ExecStart=/root/FOCS_STUFFS/FOCS_Admin/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 'app:create_app()'
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

**Save and exit** (Ctrl+X, then Y, then Enter)

---

## Step 4: Enable and Start Service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service to start on boot
sudo systemctl enable ai_labs

# Start the service
sudo systemctl start ai_labs

# Check status
sudo systemctl status ai_labs
```

**Expected output:**
```
● ai_labs.service - AI Labs Admin Panel
   Active: active (running)
```

---

## Step 5: Configure Nginx

```bash
# Create nginx config
sudo nano /etc/nginx/sites-available/ai_labs
```

**Paste this configuration:**

```nginx
server {
    listen 80;
    server_name your-domain.com;  # Change to your domain or IP

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /root/FOCS_STUFFS/FOCS_Admin/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

**Save and exit**

```bash
# Enable the site
sudo ln -s /etc/nginx/sites-available/ai_labs /etc/nginx/sites-enabled/

# Remove default site (optional)
sudo rm /etc/nginx/sites-enabled/default

# Test nginx configuration
sudo nginx -t

# Restart nginx
sudo systemctl restart nginx
```

---

## Step 6: Configure Firewall

```bash
# Allow HTTP
sudo ufw allow 80/tcp

# Allow HTTPS (for future SSL)
sudo ufw allow 443/tcp

# Allow SSH (important!)
sudo ufw allow 22/tcp

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status
```

---

## Step 7: Verify Deployment

### Check if app is running:
```bash
curl http://localhost:8000/admin/login
```

### Check from outside:
```bash
curl http://YOUR_SERVER_IP/admin/login
```

### Access in browser:
```
http://YOUR_SERVER_IP/admin/login
```

**Login credentials:**
- Username: `admin`
- Password: `admin123`

---

## 🔧 Management Commands

### View logs:
```bash
sudo journalctl -u ai_labs -f
```

### Restart application:
```bash
sudo systemctl restart ai_labs
```

### Stop application:
```bash
sudo systemctl stop ai_labs
```

### Check application status:
```bash
sudo systemctl status ai_labs
```

---

## 🔄 Update Application

```bash
cd /root/FOCS_STUFFS/FOCS_Admin
git pull origin main
sudo systemctl restart ai_labs
```

---

## 🔒 Add SSL Certificate (Optional)

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal is configured automatically
```

---

## 🐛 Troubleshooting

### Application not starting:
```bash
# Check logs
sudo journalctl -u ai_labs -n 50

# Check if port 8000 is in use
sudo netstat -tulpn | grep 8000

# Manual test
cd /root/FOCS_STUFFS/FOCS_Admin
source venv/bin/activate
python app.py
```

### Nginx errors:
```bash
# Check nginx error log
sudo tail -f /var/log/nginx/error.log

# Test nginx config
sudo nginx -t
```

### Permission issues:
```bash
# Fix permissions
cd /root/FOCS_STUFFS
chmod -R 755 FOCS_Admin
```

---

## 📝 Environment Variables (Optional)

```bash
cd /root/FOCS_STUFFS/FOCS_Admin
nano .env
```

Add:
```env
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=false
PORT=8000
```

---

## ✅ Complete Deployment Script

Copy-paste this entire script to deploy in one go:

```bash
#!/bin/bash

# Update system
sudo apt update && sudo apt upgrade -y

# Install packages
sudo apt install python3 python3-pip python3-venv nginx git -y

# Create directory and clone
cd /root
mkdir -p FOCS_STUFFS
cd FOCS_STUFFS
git clone https://github.com/itscodercamp/FOCS_Admin.git
cd FOCS_Admin

# Setup venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Create systemd service
sudo tee /etc/systemd/system/ai_labs.service > /dev/null <<EOF
[Unit]
Description=AI Labs Admin Panel - Gunicorn Application
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/root/FOCS_STUFFS/FOCS_Admin
Environment="PATH=/root/FOCS_STUFFS/FOCS_Admin/venv/bin"
ExecStart=/root/FOCS_STUFFS/FOCS_Admin/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 'app:create_app()'
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable ai_labs
sudo systemctl start ai_labs

# Create nginx config
sudo tee /etc/nginx/sites-available/ai_labs > /dev/null <<EOF
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /static/ {
        alias /root/FOCS_STUFFS/FOCS_Admin/static/;
        expires 30d;
    }
}
EOF

# Enable nginx site
sudo ln -s /etc/nginx/sites-available/ai_labs /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

# Configure firewall
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
echo "y" | sudo ufw enable

echo "✅ Deployment Complete!"
echo "🌐 Access at: http://YOUR_SERVER_IP/admin/login"
echo "👤 Username: admin"
echo "🔑 Password: admin123"
```

Save this as `deploy.sh`, make it executable, and run:

```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 🎉 Done!

Your application is now live at:
- **URL**: `http://YOUR_SERVER_IP/admin/login`
- **Username**: `admin`
- **Password**: `admin123`

**⚠️ Important:** Change the admin password after first login!

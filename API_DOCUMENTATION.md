# AI Labs Portal - Updated API Documentation

## Base URL
```
https://steve5911.pythonanywhere.com
```

---

## 📌 API Endpoints

### 1. Contact Form (General Inquiry)

**Endpoint:** `/api/contact`
**Method:** `POST`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "type": "Business Inquiry",
  "message": "Hello, I need software..."
}
```

**Success Response (201):**
```json
{
  "message": "Contact query submitted successfully"
}
```

---

### 2. AI Labs Partnership (College/Institution)

**Endpoint:** `/api/academy/partnership`
**Method:** `POST`

**Request Body:**
```json
{
  "collegeName": "RCOEM",
  "email": "principal@rcoem.edu",
  "phone": "9876543210"
}
```

**Success Response (201):**
```json
{
  "message": "Partnership request submitted successfully"
}
```

---

### 3. Job Application (Careers)

**Endpoint:** `/api/careers/apply`
**Method:** `POST`

**Request Body:**
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "resumeLink": "https://linkedin.com/in/jane",
  "coverLetter": "I am a good fit because...",
  "jobRole": "Senior Full Stack Developer"
}
```

**Success Response (201):**
```json
{
  "message": "Job application submitted successfully"
}
```

---

### 4. Projects (Student Showcases)

#### 4.1. Get All Projects

**Endpoint:** `/api/projects`
**Method:** `GET`

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "AgriTech AI",
    "studentName": "Aarav Patel",
    "college": "VNIT",
    "year": "4th Year",
    "description": "Smart agriculture platform...",
    "fullDescription": "Detailed description of the project...",
    "duration": "3 Months",
    "techStack": ["Flutter", "Python", "TensorFlow"],
    "thumbnail": "https://image-url.com/thumb.jpg",
    "screenshots": ["https://image.com/1.jpg", "https://image.com/2.jpg"],
    "liveLink": "https://agritech.app",
    "repoLink": "https://github.com/...",
    "timestamp": "2023-12-01T10:30:00"
  }
]
```

#### 4.2. Add New Project (Admin)

**Endpoint:** `/api/projects`
**Method:** `POST`

**Request Body:**
```json
{
  "title": "AgriTech AI",
  "studentName": "Aarav Patel",
  "college": "VNIT",
  "year": "4th Year",
  "description": "Short summary for card...",
  "fullDescription": "Detailed description...",
  "duration": "3 Months",
  "techStack": ["Flutter", "Python", "TensorFlow"],
  "thumbnail": "https://image-url.com/thumb.jpg",
  "screenshots": ["https://image.com/1.jpg", "https://image.com/2.jpg"],
  "liveLink": "https://agritech.app",
  "repoLink": "https://github.com/..."
}
```

**Success Response (201):**
```json
{
  "message": "Project added successfully",
  "id": 1
}
```

---

### 5. Events & Workshops

#### 5.1. Get All Events

**Endpoint:** `/api/events`
**Method:** `GET`

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "GenAI Workshop",
    "category": "Workshop",
    "date": "Dec 15, 2023",
    "time": "10:00 AM",
    "venue": "Main Auditorium",
    "organizer": "FOCS Team",
    "shortDesc": "Introduction to Generative AI...",
    "fullDesc": "Detailed workshop description...",
    "mainImage": "https://image-url.com/banner.jpg",
    "gallery": ["https://img1.jpg", "https://img2.jpg"],
    "timestamp": "2023-11-20T09:00:00"
  }
]
```

#### 5.2. Add New Event (Admin)

**Endpoint:** `/api/events`
**Method:** `POST`

**Request Body:**
```json
{
  "title": "GenAI Workshop",
  "category": "Workshop",
  "date": "Dec 15, 2023",
  "time": "10:00 AM",
  "venue": "Auditorium",
  "organizer": "FOCS Team",
  "shortDesc": "Short summary...",
  "fullDesc": "Detailed description...",
  "mainImage": "https://image-url.com/banner.jpg",
  "gallery": ["https://img1.jpg", "https://img2.jpg"]
}
```

**Success Response (201):**
```json
{
  "message": "Event added successfully",
  "id": 1
}
```

---

## 🧪 Testing Examples

### Using JavaScript Fetch (Projects)

```javascript
// Get all projects
const projects = await fetch('https://steve5911.pythonanywhere.com/api/projects');
const data = await projects.json();
console.log(data);

// Add new project
const response = await fetch('https://steve5911.pythonanywhere.com/api/projects', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    title: "Smart Campus",
    studentName: "Rahul Sharma",
    college: "IIT Delhi",
    year: "Final Year",
    description: "IoT-based campus management system",
    fullDescription: "Complete automation...",
    duration: "6 Months",
    techStack: ["React", "Node.js", "MongoDB", "Arduino"],
    thumbnail: "https://example.com/thumb.jpg",
    screenshots: ["https://example.com/1.jpg"],
    liveLink: "https://smartcampus.com",
    repoLink: "https://github.com/rahul/smart-campus"
  })
});
```

### Using cURL (Events)

```bash
# Get all events
curl https://steve5911.pythonanywhere.com/api/events

# Add new event
curl -X POST https://steve5911.pythonanywhere.com/api/events \
  -H "Content-Type: application/json" \
  -d '{
    "title": "AI Hackathon 2024",
    "category": "Hackathon",
    "date": "Jan 20, 2024",
    "time": "9:00 AM",
    "venue": "Tech Park",
    "organizer": "FOCS",
    "shortDesc": "24-hour AI hackathon",
    "fullDesc": "Build AI solutions for real-world problems",
    "mainImage": "https://example.com/banner.jpg",
    "gallery": ["https://example.com/1.jpg", "https://example.com/2.jpg"]
  }'
```

---

## 📝 Summary of All Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/contact` | POST | Submit contact inquiry |
| `/api/academy/partnership` | POST | Submit partnership request |
| `/api/careers/apply` | POST | Submit job application |
| `/api/projects` | GET | Fetch all projects |
| `/api/projects` | POST | Add new project |
| `/api/events` | GET | Fetch all events |
| `/api/events` | POST | Add new event |

---

## ✅ CORS Enabled

CORS is now enabled for all `/api/*` routes. Frontend can call from any domain.

---

## 📞 Admin Panel

**URL:** https://steve5911.pythonanywhere.com/admin/login
**Credentials:** `admin` / `admin123`

From the admin panel, you can:
- View and delete Contact Inquiries
- View and delete Partnership Requests
- View and delete Job Applications
- **View, add, and delete Projects**
- **View, add, and delete Events**

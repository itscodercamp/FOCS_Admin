# 🚀 AI Labs Portal - Comprehensive API Documentation

## 🌐 Base URL
```
http://82.29.165.213:5000
```

---

## 📌 API Endpoints Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/contact` | POST | Submit contact inquiry |
| `/api/academy/partnership` | POST | Submit partnership request |
| `/api/careers/apply` | POST | Submit job application |
| `/api/vacancies` | GET | Fetch all active job vacancies |
| `/api/vacancies` | POST | Add new job vacancy (Admin) |
| `/api/projects` | GET | Fetch all projects |
| `/api/projects` | POST | Add new project (Admin) |
| `/api/events` | GET | Fetch all events |
| `/api/events` | POST | Add new event (Admin) |

---

## 🛠️ Detailed Endpoint Documentation

### 1. Job Vacancies (New ✨)

#### 1.1. Get All Vacancies
**Endpoint:** `/api/vacancies`  
**Method:** `GET`

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "Full Stack Developer",
    "slug": "full-stack-developer",
    "location": "Remote / Nagpur",
    "type": "Full Time",
    "description": "We are looking for...",
    "requirements": ["React", "Python", "Flask"],
    "timestamp": "2024-02-13T10:00:00"
  }
]
```

#### 1.2. Add New Vacancy (Admin)
**Endpoint:** `/api/vacancies`  
**Method:** `POST`

**Request Body:**
```json
{
  "title": "UI/UX Designer",
  "location": "Nagpur",
  "type": "Internship",
  "description": "Designing modern interfaces...",
  "requirements": ["Figma", "Adobe XD"]
}
```

---

### 2. Job Application (Careers)

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

---

### 3. Contact Form (General Inquiry)

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

---

### 4. AI Labs Partnership (College/Institution)

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

---

### 5. Projects (Student Showcases)

#### 5.1. Get All Projects
**Endpoint:** `/api/projects`  
**Method:** `GET`

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "AgriTech AI",
    "studentName": "Aarav Patel",
    "techStack": ["Flutter", "Python", "TensorFlow"],
    "thumbnail": "https://image-url.com/thumb.jpg"
  }
]
```

---

### 6. Events & Workshops

#### 6.1. Get All Events
**Endpoint:** `/api/events`  
**Method:** `GET`

**Success Response (200):**
```json
[
  {
    "id": 1,
    "title": "GenAI Workshop",
    "category": "Workshop",
    "date": "Dec 15, 2023"
  }
]
```

---

## 🧪 Integration & Testing

### 1. API Testing Dashboard
You can test all APIs visually at:
`http://82.29.165.213:5000/test-api`

### 2. Reusable JS Module (`static/js/api.js`)
We have a modular API handler for the frontend:
- `getVacancies()`
- `submitCareerForm(formData)`
- `submitContactForm(formData)`
- `getProjects()`
- `getEvents()`

---

## � Admin Panel
**URL:** `http://82.29.165.213:5000/admin/login`  
**Credentials:** `admin` / `admin123`

---

## ✅ CORS Enabled
CORS is enabled for all `/api/*` routes. Frontend can call from any domain.

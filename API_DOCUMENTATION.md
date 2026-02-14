# 🚀 AI Labs Portal - Official API Documentation (Final)

## 🌐 Server Details
*   **Base URL:** `https://apis.focsit.in`
*   **API Root:** `https://apis.focsit.in/api`
*   **Image/Static Root:** `https://apis.focsit.in` (No `/api` prefix for images)

---

## 🖼️ Special Instruction: Handling Images
Backend se images ke relative paths milte hain (e.g., `/static/uploads/events/img.jpg`).
**Frontend fix:** Har image URL ke aage Base URL lagana compulsory hai.
*   **Correct URL:** `https://apis.focsit.in/static/uploads/events/your_image.jpg`

---

## 📌 1. Job Vacancies (Careers Page)

### **Get All Active Jobs**
*   **Endpoint:** `/api/vacancies`
*   **Method:** `GET`
*   **Purpose:** Frontend par available jobs dikhane ke liye.
*   **Response Body:**
```json
[
  {
    "id": 1,
    "title": "Full Stack Developer",
    "location": "Remote",
    "type": "Full Time",
    "description": "Job description here...",
    "requirements": "React, Python, Flask",
    "timestamp": "2024-02-14T10:00:00"
  }
]
```

---

## 📌 2. Form Submissions

### **2.1. Submit Job Application**
*   **Endpoint:** `/api/careers/apply`
*   **Method:** `POST`
*   **Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "jobRole": "Full Stack Developer",
  "resumeLink": "https://drive.google.com/...",
  "coverLetter": "Interested in working..."
}
```

### **2.2. Contact Form**
*   **Endpoint:** `/api/contact`
*   **Method:** `POST`
*   **Request Body:**
```json
{
  "name": "Jane User",
  "email": "jane@example.com",
  "type": "General Inquiry",
  "message": "Hello, I want to know about..."
}
```

### **2.3. Partnership Request**
*   **Endpoint:** `/api/academy/partnership`
*   **Method:** `POST`
*   **Request Body:**
```json
{
  "collegeName": "RCOEM Nagpur",
  "email": "principal@rcoem.edu",
  "phone": "9876543210"
}
```

---

## 📌 3. Content Showcase

### **3.1. Projects (Student Showcases)**
*   **Get All Projects:** `GET /api/projects`
*   **Get Single Project:** `GET /api/projects/<id_or_slug>`
*   **Important Fields:** `thumbnail` (main image URL), `screenshots` (comma-separated URL list).

### **3.2. Events & Workshops**
*   **Get All Events:** `GET /api/events`
*   **Get Single Event:** `GET /api/events/<id_or_slug>`
*   **Important Fields:** `main_image` (banner URL), `gallery` (comma-separated URL list).

---

## 🧪 Testing & Debugging
1.  **Visual Testing Dashboard:** `https://apis.focsit.in/test-api`
2.  **Admin Login:** `https://apis.focsit.in/admin/login`
3.  **CORS:** Enabled for all domains.

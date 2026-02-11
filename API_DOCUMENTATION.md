# AI Labs Portal - API Documentation

## Base URL
```
https://steve5911.pythonanywhere.com
```

---

## 📌 API Endpoints

### 1. Contact Form (General Inquiry)

**Purpose:** Submit general contact inquiries from users.

**Endpoint:** `/api/contact`

**Method:** `POST`

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "name": "User Name",
  "email": "user@example.com",
  "type": "Service Type (e.g., Web Dev, AI Services, Support)",
  "message": "User message here..."
}
```

**Example Request (JavaScript Fetch):**
```javascript
const response = await fetch('https://steve5911.pythonanywhere.com/api/contact', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: "Rahul Sharma",
    email: "rahul@example.com",
    type: "Web Dev",
    message: "I need help with my website development."
  })
});

const data = await response.json();
console.log(data);
```

**Example Request (Axios):**
```javascript
const response = await axios.post('https://steve5911.pythonanywhere.com/api/contact', {
  name: "Rahul Sharma",
  email: "rahul@example.com",
  type: "Web Dev",
  message: "I need help with my website development."
});

console.log(response.data);
```

**Success Response (201 Created):**
```json
{
  "message": "Contact query submitted successfully"
}
```

**Error Response (400/500):**
```json
{
  "error": "Error message here"
}
```

---

### 2. AI Labs Partnership (College/Institution)

**Purpose:** Submit partnership requests from colleges/institutions for AI Labs.

**Endpoint:** `/api/academy/partnership`

**Method:** `POST`

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "collegeName": "ABC Engineering College",
  "email": "principal@college.edu",
  "phone": "9876543210"
}
```

**Example Request (JavaScript Fetch):**
```javascript
const response = await fetch('https://steve5911.pythonanywhere.com/api/academy/partnership', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    collegeName: "Delhi Technological University",
    email: "dean@dtu.ac.in",
    phone: "9811223344"
  })
});

const data = await response.json();
console.log(data);
```

**Example Request (Axios):**
```javascript
const response = await axios.post('https://steve5911.pythonanywhere.com/api/academy/partnership', {
  collegeName: "Delhi Technological University",
  email: "dean@dtu.ac.in",
  phone: "9811223344"
});

console.log(response.data);
```

**Success Response (201 Created):**
```json
{
  "message": "Partnership request submitted successfully"
}
```

**Error Response (400/500):**
```json
{
  "error": "Error message here"
}
```

---

### 3. Job Application (Careers)

**Purpose:** Submit job applications for open positions.

**Endpoint:** `/api/careers/apply`

**Method:** `POST`

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "jobRole": "Senior Full Stack Developer",
  "name": "Candidate Name",
  "email": "candidate@email.com",
  "resumeLink": "https://drive.google.com/file/...",
  "coverLetter": "I am a good fit because..."
}
```

**Example Request (JavaScript Fetch):**
```javascript
const response = await fetch('https://steve5911.pythonanywhere.com/api/careers/apply', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    jobRole: "Senior Full Stack Developer",
    name: "Vikram Singh",
    email: "vikram@example.com",
    resumeLink: "https://linkedin.com/in/vikram-singh",
    coverLetter: "I have 5 years of MERN stack experience..."
  })
});

const data = await response.json();
console.log(data);
```

**Example Request (Axios):**
```javascript
const response = await axios.post('https://steve5911.pythonanywhere.com/api/careers/apply', {
  jobRole: "Senior Full Stack Developer",
  name: "Vikram Singh",
  email: "vikram@example.com",
  resumeLink: "https://linkedin.com/in/vikram-singh",
  coverLetter: "I have 5 years of MERN stack experience..."
});

console.log(response.data);
```

**Success Response (201 Created):**
```json
{
  "message": "Job application submitted successfully"
}
```

**Error Response (400/500):**
```json
{
  "error": "Error message here"
}
```

---

## 🔒 CORS Information

The API currently does **NOT** have CORS enabled. If you're calling from a different domain (frontend), you may encounter CORS errors. 

**Solution:** Request the backend admin to add CORS headers or use a proxy.

---

## 📝 Field Validations

### Contact Form
- `name`: Required, string
- `email`: Required, valid email format
- `type`: Optional, string (e.g., "Web Dev", "AI Services")
- `message`: Required, string

### Partnership Form
- `collegeName`: Required, string
- `email`: Required, valid email format
- `phone`: Required, string (10 digits recommended)

### Careers Form
- `jobRole`: Required, string
- `name`: Required, string
- `email`: Required, valid email format
- `resumeLink`: Optional, string (URL)
- `coverLetter`: Optional, string

---

## 🧪 Testing the API

### Using cURL:

**Contact API:**
```bash
curl -X POST https://steve5911.pythonanywhere.com/api/contact \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","type":"Testing","message":"This is a test message"}'
```

**Partnership API:**
```bash
curl -X POST https://steve5911.pythonanywhere.com/api/academy/partnership \
  -H "Content-Type: application/json" \
  -d '{"collegeName":"Test College","email":"test@college.edu","phone":"1234567890"}'
```

**Careers API:**
```bash
curl -X POST https://steve5911.pythonanywhere.com/api/careers/apply \
  -H "Content-Type: application/json" \
  -d '{"jobRole":"Developer","name":"Test Candidate","email":"candidate@test.com","resumeLink":"https://example.com","coverLetter":"Test letter"}'
```

### Using Postman:
1. Set method to `POST`
2. Enter the endpoint URL
3. Go to **Headers** tab, add: `Content-Type: application/json`
4. Go to **Body** tab, select **raw** and **JSON**
5. Paste the request body
6. Click **Send**

---

## ⚠️ Error Codes

| Status Code | Meaning |
|------------|---------|
| 200 | OK - Request successful (not used in these APIs) |
| 201 | Created - Data submitted successfully |
| 400 | Bad Request - Missing or invalid data |
| 500 | Internal Server Error - Server-side issue |

---

## 📞 Support

For API issues or questions, contact the backend team or check the admin panel logs.

**Admin Panel URL:** https://steve5911.pythonanywhere.com/admin/login

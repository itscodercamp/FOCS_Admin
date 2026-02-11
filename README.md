# AI Labs Admin Panel - Setup & Usage

## Overview
This is a dedicated **Admin Panel** for managing usage of the AI Labs services. The public frontend has been removed, and the root URL now redirects to the admin login.

## Features
- **Secure Login**: Admin authentication required.
- **Dedicated Tabs**:
    - **Contact Inquiries**: View and delete general messages.
    - **Partnership Requests**: Manage college partnership applications.
    - **Job Applications**: Review career applications (resume links, cover letters).
- **CRUD Operations**: Admins can view details and delete any record.

## Technical Details
- **Backend**: Flask
- **Database**: SQLite
- **Frontend**: Custom HTML/CSS (No external framework dependencies)

## How to Run
1.  **Activate Virtual Environment**:
    ```powershell
    .\venv\Scripts\activate
    ```
2.  **Run Application**:
    ```powershell
    python app.py
    ```
3.  **Access Admin Panel**:
    - URL: `http://127.0.0.1:5000/` (Redirects to Login)
    - **Username**: `admin`
    - **Password**: `admin123`

## API Endpoints
The following endpoints are active for data ingestion (e.g., from an external frontend or mobile app):
- `POST /api/contact`
- `POST /api/academy/partnership`
- `POST /api/careers/apply`

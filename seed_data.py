import requests
import json
import random

BASE_URL = "http://127.0.0.1:5000/api"

def print_response(response, name):
    if response.status_code == 201:
        print(f"[SUCCESS] {name} created.")
    else:
        print(f"[ERROR] Failed to create {name}. Status: {response.status_code}, Body: {response.text}")

# 1. Contact Queries
contacts = [
    {
        "name": "Rahul Sharma",
        "email": "rahul.sharma@example.com",
        "type": "General Inquiry",
        "message": "Hi, I would like to know more about your AI services for small businesses."
    },
    {
        "name": "Priya Patel",
        "email": "priya.p@test.com",
        "type": "Technical Support",
        "message": "I am facing issues with the API integration. Can you help?"
    },
    {
        "name": "Amit Kumar",
        "email": "amit.k@webdev.in",
        "type": "Sales",
        "message": "We are interested in a bulk license for your software."
    }
]

print("--- Seeding Contact Queries ---")
for data in contacts:
    response = requests.post(f"{BASE_URL}/contact", json=data)
    print_response(response, f"Contact ({data['name']})")

# 2. Partnership Requests
partnerships = [
    {
        "collegeName": "Delhi Technological University",
        "email": "dean.tie@dtu.ac.in",
        "phone": "9811223344"
    },
    {
        "collegeName": "IIT Bombay",
        "email": "placement@iitb.ac.in",
        "phone": "9876500001"
    }
]

print("\n--- Seeding Partnership Requests ---")
for data in partnerships:
    response = requests.post(f"{BASE_URL}/academy/partnership", json=data)
    print_response(response, f"Partnership ({data['collegeName']})")

# 3. Job Applications
jobs = [
    {
        "jobRole": "Senior Full Stack Developer",
        "name": "Vikram Singh",
        "email": "vikram.s@coder.com",
        "resumeLink": "https://linkedin.com/in/vikram-singh-dev",
        "coverLetter": "I have 5 years of experience in MERN stack and Flask. I built..."
    },
    {
        "jobRole": "AI Research Scientist",
        "name": "Neha Gupta",
        "email": "neha.g@ai-research.org",
        "resumeLink": "https://github.com/nehagupta/resume.pdf",
        "coverLetter": "My research focuses on NLP and Transformers. I have published..."
    }
]

print("\n--- Seeding Job Applications ---")
for data in jobs:
    response = requests.post(f"{BASE_URL}/careers/apply", json=data)
    print_response(response, f"Job App ({data['name']})")

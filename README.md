# Django Task Project

This project is a **Django + Django REST Framework (DRF)** based application that demonstrates how to fetch and serve complex SQL data through clean ORM queries and REST APIs.

---

## 🚀 Project Overview

The project connects multiple related database tables — such as `Company`, `Company_Executives`, `Persons`, and `LinkedIn_Person` — and exposes structured data using Django REST API endpoints.

It includes **five queries** (SQL + ORM) implemented in **views** and **utils**, each fetching specific business information.

---

## Project Structure

| File / Folder | Description |
|----------------|-------------|
| **mysite/** | Main Django project folder (settings, URLs, etc.) |
| **polls/** | Core app containing models, views, serializers, utils, and API endpoints |
| **logs.py** | Centralized logging setup used by views and utilities |
| **polls/models.py** | Contains ORM model definitions mapped to database tables (e.g., Company, Persons, LinkedInPerson, etc.) |
| **polls/serializers.py** | Converts model data to JSON format for REST APIs |
| **polls/views.py** | Handles API requests, calls utility functions, and returns responses |
| **polls/utils.py** | Contains reusable ORM functions that run SQL-equivalent queries |
| **polls/urls.py** | Maps API routes to corresponding views |
| **requirements.txt** | Lists all dependencies (Django, DRF, etc.) |
| **manage.py** | Django command-line entry point |
| **README.md** | Project documentation (this file) |

---


## Queries Implemented

### **1. PremiumUsersView**
**Displays:**  
The List of premium users and their personality.

---

### **2. ActivePremiumUsersView**
**Displays:**  
List of users with having premium licenses of xiQ.

---
### **3. CompanyRevenueView**
**Displays:**  
A list of companies showing their name, website, industry, and most recent revenue.

---
### **4. ExecutivesInfoView**
**Displays:**  
For selected companies, lists their **executives**, showing the executive’s name, job title, and LinkedIn profile URL.

---

### **5. DigestEmailStatsView**
**Displays:**  
The stats for that email. i.e. open count, click count total recipient email sent.

---

## 🔗 API Endpoints

| Endpoint | Method |*
|-----------|---------|-------------|
| `/api/premium-users/` | GET | 
| `/api/active-premium-users/` | GET | 
| `/api/company-revenue/` | GET | 
| `/api/executives-info/` | GET | 
| `/api/digest-stats/` | GET |

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/zhussain123/django-task-project.git
   cd django-task-project

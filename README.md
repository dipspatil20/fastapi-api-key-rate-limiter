# 🔐 API Key & Rate Limiting Service (FastAPI)

## 📌 Project Overview

This project is a backend service built using FastAPI that provides:

* API key generation for clients
* Secure access to protected APIs
* Request tracking per API key
* Rate limiting (5 requests per minute)

---

## ⚙️ Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Pydantic

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🔑 API Endpoints

### 1. Generate API Key

* **POST** `/generate-key`
* No request body required

**Response:**

```json
{
  "key": "your_api_key",
  "created_at": "timestamp"
}
```

---

### 2. Access Protected API

* **GET** `/data`

**Headers required:**

```
x-api-key: your_api_key
```

**Response:**

```json
{
  "message": "Access granted",
  "data": "This is protected data"
}
```

---

## ⏱️ Rate Limiting

* Each API key is limited to **5 requests per minute**
* If limit exceeded → returns:

```json
{
  "detail": "Rate limit exceeded. Try again later."
}
```

---

## 🗄️ Database

* SQLite database (`test.db`)
* Stores:

  * API key
  * Created time
  * Request count
  * Last request timestamp

---

## 📂 Project Structure

```
project/
│
├── routes/
│   ├── auth.py
│   ├── protected.py
│
├── utils/
│   ├── rate_limiter.py
│   ├── security.py
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── requirements.txt
├── README.md
├── postman/
│   └── postman_collection.json
```

---

## 📬 Postman Collection

* Included in `postman/postman_collection.json`
* Contains:

  * Generate API Key request
  * Protected API request

---

## ✅ Features Implemented

* Secure API key generation
* Per-user request tracking
* Time-based rate limiting
* Protected endpoint with authentication
* Swagger documentation (`/docs`)

---

## 🎯 Summary

This project demonstrates how to build a secure backend system with API authentication and rate limiting using FastAPI.

---

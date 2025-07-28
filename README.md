# 🧩 Fullstack FastAPI and React Application

A modern fullstack web application built with **FastAPI** for the backend and **React** with **Vite** for the frontend. This project includes authentication, history tracking, challenge modules, and a responsive layout.

---

## 🚀 Features

### 🔐 Authentication
- Implemented with [Clerk](https://clerk.com/) for secure user login, signup, and session management.

### 🧠 Challenge System
- Allows users to interact with various challenges through a dynamic interface.

### 📜 History Tracking
- Tracks user activities and logs them in the history section.

### 🌐 Fullstack Integration
- API built using FastAPI.
- Frontend built with React + Vite.
- Secure API routing and database management using modular architecture.

---

## 📁 Folder Structure
.
├── backend
│ ├── .venv
│ └── src
│ ├── database
│ ├── routes
│ ├── pyproject.toml
│ └── uv.lock
├── frontend
│ ├── node_modules
│ ├── public
│ └── src
│ ├── auth
│ ├── challenge
│ ├── history
│ ├── layout
│ └── utils
│ ├── App.jsx
│ ├── index.css
│ ├── main.jsx
├── .env
├── .gitignore
├── index.html
├── vite.config.js
├── README.md


---

## 🛠️ Technologies Used

### Backend
- **FastAPI** 🐍
- **Uvicorn** as ASGI server
- **SQLite/PostgreSQL** (depending on environment)
- **Pydantic** for data validation

### Frontend
- **React 19**
- **React Router DOM**
- **Vite** for fast bundling
- **Clerk** for authentication
- **Tailwind CSS / CSS Modules** (optional for styling)

---

## 🧪 Setup Instructions

### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/OntongGhebi/Fullstack-FastAPIandReact.git
   cd Fullstack-FastAPIandReact/backend


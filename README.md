<div align="center">
  <img src="https://raw.githubusercontent.com/fastapi/fastapi/master/docs/en/docs/img/logo-margin/logo-teal.png" width="120" alt="FastAPI Logo"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" width="120" alt="React Logo"/>
  <h1>🚀 Fullstack Code Challenge Generator</h1>
  <p><i>A modern web application for generating, solving, and tracking coding challenges — powered by <b>FastAPI</b> & <b>React</b>.</i></p>
</div>

---

## ✨ Features

- 🔐 **Authentication** with Clerk (secure login & session handling)  
- 💻 **Code Challenge System**: dynamic challenge navigation & submission  
- 📜 **History Tracking**: log & display past attempts  
- ⚡ **Fullstack Integration**: clean separation of backend (FastAPI) & frontend (React + Vite)  
- 🌐 **Ngrok Support**: expose local server securely for external access  

---

## 🛠️ Tech Stack

**Backend**
- ⚡ FastAPI + Uvicorn  
- 🗄️ SQLite / PostgreSQL  
- 📦 Pydantic for validation  

**Frontend**
- ⚛️ React 19 + Vite  
- 🎨 Tailwind CSS / CSS Modules  
- 🔑 Clerk Authentication  
- 🔀 React Router DOM  

**Tools**
- 🌐 Ngrok (tunnel local dev server)  
- 🐙 Git + GitHub  

---

/backend
 ├── app/
 │   ├── main.py
 │   ├── routers/
 │   ├── models/
 │   └── schemas/
 └── requirements.txt

/frontend
 ├── src/
 │   ├── components/
 │   ├── pages/
 │   ├── App.jsx
 │   └── main.jsx
 ├── public/
 └── package.json

---

## ⚡ Quick Start

### Prerequisites
- `Python 3.10+`
- `Node.js (npm/yarn)`
- `ngrok` account & CLI installed

---

### 1️⃣ Clone Repo
```bash
git clone https://github.com/OntongGhebi/Fullstack-FastAPIandReact.git
cd Fullstack-FastAPIandReact

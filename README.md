# ✅ Full-Stack To-Do App (DRF & React)

A complete task management application featuring a **Django REST Framework** backend and a **React** frontend. This project demonstrates full CRUD (Create, Read, Update, Delete) functionality, utilizing class-based components and state management in React to interact with a RESTful API.

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework (DRF).
* **Frontend:** React.js (Class Components, Constructors).
* **Database:** SQLite (default Django).
* **API:** RESTful architecture with JSON serialization.

---

## 📂 Project Structure

### Backend (Django)

* **Serializers**: Converts `Task` model instances into JSON format for the frontend.
* **Function-Based Views**: API views using the `@api_view` decorator to handle GET, POST, and DELETE methods.
* **URL Routing**: Clean API endpoints (e.g., `/api/task-list/`, `/api/task-create/`).

### Frontend (React)

* **Constructors**: Used to initialize component state and bind event handlers.
* **Lifecycle Methods**: `componentDidMount` is used to fetch initial data from the API.
* **CSRF Handling**: Logic to handle Django's CSRF tokens for secure POST requests.

---

## 🚀 Features & API Endpoints

| Action | Method | Endpoint | Logic |
| --- | --- | --- | --- |
| **List Tasks** | `GET` | `/api/task-list/` | Fetches all tasks from the DB. |
| **Add Task** | `POST` | `/api/task-create/` | Saves a new task object. |
| **Update Task** | `POST` | `/api/task-update/<id>/` | Modifies an existing task instance. |
| **Delete Task** | `DELETE` | `/api/task-delete/<id>/` | Removes a task from the DB. |

---

## ⚙️ Setup Instructions

### Backend Setup

1. **Install dependencies**:
```bash
pip install django djangorestframework django-cors-headers

```


2. **Apply migrations**:
```bash
python manage.py makemigrations
python manage.py migrate

```


3. **Start the API**:
```bash
python manage.py runserver

```



### Frontend Setup

1. **Navigate to frontend folder**:
```bash
cd frontend

```


2. **Install NPM packages**:
```bash
npm install

```


3. **Start the React app**:
```bash
npm start

```



---

## 📝 Usage Note on React Components

The frontend utilizes **Class Components**. In the **Constructor**, the initial state is defined to track the `todoList` and the `activeItem` currently being edited.

```javascript
constructor(props){
  super(props);
  this.state = {
    todoList: [],
    activeItem: { id: null, title: '', completed: false },
    editing: false,
  }
  this.fetchTasks = this.fetchTasks.bind(this);
}

```


Would you like me to add a section on how to handle **CORS (Cross-Origin Resource Sharing)** so your React app can talk to your Django server without errors?

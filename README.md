# Django Kanban & Image Annotation API

This repository contains the backend for a 2-in-1 web application that combines a task management system (Kanban board) and an image annotation tool. Built with Django and Django REST Framework, it provides a secure, robust, and scalable RESTful API with interactive OpenAPI 3 (Swagger & ReDoc) documentation.

---

## 📖 Interactive API Documentation

Once the server is running, you can explore, test, and view interactive documentation for all endpoints:

- **Swagger UI (Interactive API Explorer)**: [`/api/docs/`](https://kanban-backend-4apg.onrender.com/api/docs/)
- **ReDoc (Detailed Schema Documentation)**: [`/api/redoc/`](https://kanban-backend-4apg.onrender.com/api/redoc/)
- **OpenAPI 3 Schema (YAML/JSON)**: [`/api/schema/`](https://kanban-backend-4apg.onrender.com/api/schema/)

### How to Authenticate in Swagger UI:

1. Go to `/api/auth/login/` on the Swagger UI page or send a POST request with your email and password.
2. Copy the `access` token from the response.
3. Click the green **Authorize** 🔓 button at the top right of Swagger UI.
4. In the `jwtAuth` field, enter:
   ```text
   Bearer YOUR_ACCESS_TOKEN
   ```
5. Click **Authorize** and then **Close**. Now all protected endpoints can be tested directly from the Swagger browser interface!

---

## Features

### 1. Secure Authentication

- **JWT-Based Login**: Secure user authentication using JSON Web Tokens (JWT) provided by `djangorestframework-simplejwt`.
- **User Registration**: A public endpoint for new user registration with password validation and hashing.
- **Protected Endpoints**: All API endpoints are protected by default, requiring a valid JWT for access.
- **Token Refresh**: Endpoint to refresh expired access tokens.
- **User Profile**: Endpoint to retrieve the authenticated user's profile details.

### 2. Kanban Board API

- **Task Management**: Full CRUD (Create, Read, Update, Delete) functionality for tasks.
- **Task Attributes**: Supports storing task `title`, `description`, `status` ("To Do", "In Progress", "Done"), `priority`, and `due_date`.
- **User-Specific Tasks**: Designed to associate tasks with the authenticated user.

### 3. Image Annotation API

- **Image Uploads**: Handles image uploads to cloud storage (ImageKit.io) and direct uploads.
- **Flexible Annotation Storage**: Uses Django's `JSONField` to store complex polygon annotation data, allowing for adaptable and varied shape information.
- **ImageKit Authentication**: Generates signed authentication parameters for client-side uploads.

### 4. OpenAPI 3 / Swagger Documentation

- Fully automated, interactive API documentation powered by `drf-spectacular`.
- Integrated JWT authentication directly in the UI.

---

## The Saga: Villains & Victories

Every great project has its challenges. Here are some of the villains I faced during this saga and how I overcame them with the power of friendship (with documentation, AI, and blogs!).

### The Devious CORS Monster

Our first challenge emerged when the frontend, operating from a different domain, tried to communicate with the backend. A fearsome beast known as **CORS (Cross-Origin Resource Sharing)** blocked every request, roaring "Not Allowed!" in the console. I was stumped until I summoned a powerful ally: the `django-cors-headers` library. By configuring `CORS_ALLOWED_ORIGINS` in the Django settings, I taught the backend to trust the frontend, vanquishing the CORS monster and opening the lines of communication.

### The Enigma of the Missing URL Scroll

As I built out the image annotation features, a mysterious problem occurred. While the Kanban API worked flawlessly, all requests to the annotation endpoints vanished into the ether, returning dreaded 404 errors. It was as if the routes didn't exist! The villain was an ancient, forgotten artifact: the **Missing URL Scroll**. I had created the views and models for the `annotations` app but had forgotten to include its sacred URL patterns in the main `core/urls.py` file. After a perilous journey through my own codebase, I found the scroll, added `path('api/annotations/', include('annotations.urls'))`, and restored the lost routes, making the annotation API visible to the world.

### The Shape-Shifting Data Beast

The quest required storing annotations of various shapes and sizes—polygons, rectangles, and perhaps more in the future. A rigid database schema would have crumbled under this requirement. This challenge manifested as the **Shape-Shifting Data Beast**, a creature that defied conventional data modeling. But I had a secret weapon: Django's `JSONField`. This magical field allowed me to store the shape data as a flexible JSON object, taming the beast by allowing any structure I needed. This victory ensured the application could adapt to any shape the future might throw at it.

---

## Technology Stack

- **Framework**: Django 6.0 & Django REST Framework
- **API Documentation**: `drf-spectacular` (OpenAPI 3.0 / Swagger UI / ReDoc)
- **Authentication**: `djangorestframework-simplejwt`
- **Database**: PostgreSQL (Production) / SQLite 3 (Local Development)
- **Static Files**: WhiteNoise
- **CORS Handling**: `django-cors-headers`
- **Media & Images**: ImageKit.io & Pillow

---

## Local Development Setup

To get this project running on your local machine, follow these steps.

### System Requirements

- **Python Version**: Python 3.12 or newer.

### Installation and Execution

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rakibislam22/kanban-backend.git
   cd kanban-backend
   ```

2. **Create and activate a virtual environment:**

   _On macOS/Linux:_

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   _On Windows:_

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create an environment file:**
   Create a `.env` file in the project root and add the following variables:

   ```env
   SECRET_KEY=your-super-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
   ```

5. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **(Optional) Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints Reference

### 📚 Documentation

| Method | Endpoint       | Description                              | Auth Required |
| ------ | -------------- | ---------------------------------------- | ------------- |
| `GET`  | `/api/docs/`   | Swagger UI Interactive API documentation | No            |
| `GET`  | `/api/redoc/`  | ReDoc API documentation                  | No            |
| `GET`  | `/api/schema/` | Raw OpenAPI 3 schema                     | No            |

### 🔐 Authentication (`/api/auth/`)

| Method | Endpoint                   | Description                          | Auth Required |
| ------ | -------------------------- | ------------------------------------ | ------------- |
| `POST` | `/api/auth/register/`      | Register a new user                  | No            |
| `POST` | `/api/auth/login/`         | Obtain JWT access and refresh tokens | No            |
| `POST` | `/api/auth/token/refresh/` | Refresh expired access token         | No            |
| `GET`  | `/api/auth/profile/`       | Get current logged-in user profile   | Yes (JWT)     |

### 📋 Kanban Tasks (`/api/tasks/`)

| Method   | Endpoint           | Description                     | Auth Required |
| -------- | ------------------ | ------------------------------- | ------------- |
| `GET`    | `/api/tasks/`      | List all tasks for current user | Yes (JWT)     |
| `POST`   | `/api/tasks/`      | Create a new task               | Yes (JWT)     |
| `GET`    | `/api/tasks/{id}/` | Retrieve task details           | Yes (JWT)     |
| `PUT`    | `/api/tasks/{id}/` | Update task details             | Yes (JWT)     |
| `PATCH`  | `/api/tasks/{id}/` | Partially update a task         | Yes (JWT)     |
| `DELETE` | `/api/tasks/{id}/` | Delete a task                   | Yes (JWT)     |

### 🎨 Image Annotations (`/api/`)

| Method   | Endpoint                 | Description                                    | Auth Required |
| -------- | ------------------------ | ---------------------------------------------- | ------------- |
| `GET`    | `/api/images/`           | List uploaded images                           | Yes (JWT)     |
| `POST`   | `/api/images/`           | Upload a new image (ImageKit)                  | Yes (JWT)     |
| `GET`    | `/api/annotations/`      | List annotations (filterable by `?image=<id>`) | Yes (JWT)     |
| `POST`   | `/api/annotations/`      | Create a new shape annotation                  | Yes (JWT)     |
| `GET`    | `/api/annotations/{id}/` | Retrieve annotation details                    | Yes (JWT)     |
| `PUT`    | `/api/annotations/{id}/` | Update annotation                              | Yes (JWT)     |
| `DELETE` | `/api/annotations/{id}/` | Delete annotation                              | Yes (JWT)     |
| `GET`    | `/api/imagekit-auth/`    | Get ImageKit client-side upload parameters     | No            |

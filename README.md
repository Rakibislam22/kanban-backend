# Django Kanban & Image Annotation API

This repository contains the backend for a 2-in-1 web application that combines a task management system (Kanban board) and an image annotation tool. Built with Django and Django REST Framework, it provides a secure, robust, and scalable RESTful API.

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

- **Image Uploads**: Handles multipart/form-data for image uploads.
- **Flexible Annotation Storage**: Uses Django's `JSONField` to store complex polygon annotation data, allowing for adaptable and varied shape information.

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

- **Framework**: Django & Django REST Framework
- **Authentication**: Simple JWT
- **Database**: SQLite 3 (for ease of setup)
- **Static Files**: WhiteNoise (for production environments)
- **CORS**: `django-cors-headers`

---

## Local Development Setup

To get this project running on your local machine, follow these steps.

### System Requirements

- **Python Version**: Python 3.12 or newer.

### Installation and Execution

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Rakibislam22/kanban-backend.git
    cd kanban-backend
    ```

2.  **Create and activate a virtual environment:**

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

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create an environment file:**
    Create a `.env` file in the project root and add the following variables.

    ```
    SECRET_KEY=your-super-secret-key-here
    DEBUG=True
    ```

5.  **Run database migrations:**
    This will apply the database schema for all apps.

    ```bash
    python manage.py migrate
    ```

6.  **(Optional) Create a superuser:**
    To access the Django admin panel, create a superuser.

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

A summary of the main API endpoints is provided in the API Documentation.

**Base URL**: `/api/`

- **Authentication**: `/api/auth/`
- **Kanban Tasks**: `/api/tasks/`
- **Image Annotations**: `/api/annotations/`

# Kanban & Image Annotation Backend

Welcome, brave developer, to the repository for a powerful backend forged in the fires of Django and Python. This isn't just a server; it's a dual-purpose engine designed to power both a sophisticated Kanban board and a detailed image annotation tool.

This project provides a RESTful API for:

- **Kanban Board**: Creating, updating, and managing tasks with titles, priorities, due dates, and statuses.
- **Image Annotation**: Uploading images and saving complex polygon annotations associated with them.

## The Villains We Faced

Every great saga has its villains, and the development of this backend was no different. We faced down formidable foes, armed with nothing but our wits, documentation, and the power of code.

### The Devious CORS Monster

Our first challenge emerged when our frontend, operating from a different domain, tried to communicate with the backend. A fearsome beast known as **CORS (Cross-Origin Resource Sharing)** blocked every request, roaring "Not Allowed!" in the console. We were stumped until we summoned a powerful ally: the `django-cors-headers` library. By configuring the `CORS_ALLOWED_ORIGINS` in our Django settings, we taught the backend to trust our frontend, vanquishing the CORS monster and opening the lines of communication.

### The Enigma of the Missing URL Scroll

As we built out the image annotation features, a mysterious problem occurred. While our Kanban API worked flawlessly, all requests to the annotation endpoints vanished into the ether, returning dreaded 404 errors. It was as if the routes didn't exist! The villain was an ancient, forgotten artifact: the **Missing URL Scroll**. We had created the views and models for our `annotations` app but had forgotten to include its sacred URL patterns in the main `core/urls.py` file. After a perilous journey through our own codebase, we found the scroll, added `path('api/annotations/', include('annotations.urls'))`, and restored the lost routes, making the annotation API visible to the world.

### The Shape-Shifting Data Beast

Our quest required us to store annotations of various shapes and sizes—polygons, rectangles, and perhaps more in the future. A rigid database schema would have crumbled under this requirement. This challenge manifested as the **Shape-Shifting Data Beast**, a creature that defied conventional data modeling. But we had a secret weapon: Django's `JSONField`. [40] This magical field allowed us to store the shape data as a flexible JSON object, taming the beast by allowing any structure we needed. This victory ensured our application could adapt to any shape the future might throw at it.

---

## Technical Details & Setup

To get this project running on your local machine, follow these steps.

### System Requirements

- **Python Version**: Python 3.12 or newer is recommended. The project is built with Django 6.0, which supports Python 3.12+. [1, 5]
- **Node.js**: Not required for this backend-only project.

### Installation and Execution

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Rakibislam22/kanban-backend.git
    cd kanban-backend
    ```

2.  **Create and Activate a Virtual Environment**

    _On macOS/Linux:_

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    _On Windows:_

    ```bash
    py -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all the required packages from `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Database Migrations**
    Apply the database schema for the `kanban` and `annotations` apps.

    ```bash
    python manage.py migrate
    ```

5.  **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

6.  **Access the API**
    The server will start, and you can access the API endpoints at `http://127.0.0.1:8000/`.
    - **Kanban API**: `http://127.0.0.1:8000/api/tasks/`
    - **Annotation API**: `http://127.0.0.1:8000/api/annotations/`

    You can now use a tool like Postman or `curl` to interact with your powerful new backend!

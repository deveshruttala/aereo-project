# Task Management API

This is a simple Task Management application using Django REST Framework (DRF). The API allows you to manage tasks with CRUD operations and filter tasks based on completion status and date.
Task Management API built using **Django** and **Django REST Framework**. It allows users to perform **CRUD operations** on tasks and includes features like **filtering by completion status** and **filtering by date**.

---

## 📦 Features

- ✅ Create, Read, Update, Delete (CRUD) tasks
- 🔍 Filter tasks by `completed` status
- 📅 Filter tasks by specific `date`
- 🧪 Unit tests for core API functionality using Django’s test framework
- 🧩 Modular structure following best Django practices

---

## 🚀 Quickstart

## Setup and Installation

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.8+ 
- pip (Python package manager)
- Django 4.x+
- Django REST Framework 3.x+
- Django Filter for filtering tasks

### Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/deveshruttala/aereo-project.git
cd aereo-project
```

### Step 2: Create a Virtual Environment


It’s highly recommended to create a virtual environment for the project:

```bash
python -m venv venv
```


### Step 3: Activate the Virtual Environment


- On Windows:

```bash
venv\Scripts\activate
```


- On macOS/Linux:


```bash
source venv/bin/activate
```


### Step 4: Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```



### Step 5: Apply Migrations

Run migrations to set up the database schema:

```bash
python manage.py migrate
```


### Step 6: Start the Development Server

Run the development server:

```bash
python manage.py runserver
```


##### Your API will be accessible at http://127.0.0.1:8000/


---

### Project Structure

The project consists of the following main components:

```

taskmanager/                         # Root project directory (project container)
├── manage.py                        # Django command-line utility (run server, migrations, etc.)

├── taskmanager/                     # Project configuration directory (Django project settings)
│   ├── __init__.py                  # Marks this directory as a Python package
│   ├── settings.py                  # Global Django settings (installed apps, middleware, DB config, etc.)
│   ├── urls.py                      # Main URL router pointing to app-specific routes (like /tasks/)
│   └── wsgi.py                      # WSGI entry point for production servers (e.g., Gunicorn)

├── tasks/                           # The main application for managing tasks (features live here)
│   ├── __init__.py                  # Marks this directory as a Python package
│   ├── admin.py                     # Admin interface registration (optional)
│   ├── apps.py                      # App configuration (used for setup)
│   ├── models.py                    # Defines the Task model (DB structure)
│   ├── serializers.py               # Converts model instances to JSON and validates input data
│   ├── views.py                     # ViewSets handling business logic for the API (CRUD operations)
│   ├── urls.py                      # Routes all /tasks/ endpoints to the correct views
│
│   ├── tests/                       # Contains unit and integration tests for the app
│   │   ├── __init__.py              # Makes `tests` a Python package
│   │   ├── test_views.py            # Tests for views (API endpoints)
│   │   └── test_models.py           # Tests for model logic and validation

├── requirements.txt                 # List of required Python packages to install via pip

├── Dockerfile                       # Docker setup to containerize the app
├── docker-compose.yml              # Multi-container configuration (web app + DB, etc.)
└── README.md                        # Documentation and instructions for setup, usage, and development


```


---

## Api Endpoints

The API provides several endpoints for interacting with tasks. You can access these endpoints using HTTP methods (GET, POST, PUT, DELETE) through the base URL /tasks/. Below is the description of each endpoint and how to use them.

These api endpoints can be tested in right in postman or rest_framework dashboard

### 1. List All Tasks

**URL:** `/tasks/`
**Method:** `GET`
**Description:** Retrieves a list of all tasks.
**Usage:**

To list all tasks, simply send a `GET` request to `/tasks/`.

```bash
GET http://127.0.0.1:8000/tasks/
```

### 2. Create a New Task

**URL:** `/tasks/`
**Method:** `POST`
**Description:** Creates a new task.
**Usage:**


**Example of a JSON body:**

```json
{
  "title": "New Task",
  "description": "Task description here",
  "completed": false,
  "date": "2025-05-03"
}
```

To create a new task, send a `POST` request to `/tasks/` with the task details in the request body as JSON.


```bash

POST http://127.0.0.1:8000/tasks/
Content-Type: application/json

{
  "title": "New Task",
  "description": "Task description here",
  "completed": false,
  "date": "2025-05-03"
}

```

### 3. Retrieve a Task by ID

**URL:** `/tasks/{id}/`
**Method:** `GET`
**Description:** Retrieves a specific task by its ID.
**Usage:**

To retrieve a specific task, replace `{id}` in the URL with the ID of the task you want to retrieve.

**Example:**

```bash
http://127.0.0.1:8000/tasks/1/
```


### 4. Update a Task by ID

**URL:** `/tasks/{id}/`
**Method:** `PUT`
**Description:** Updates an existing task by its ID.
**Usage:**


**Example of a JSON body:**

```json
{
  "title": "Updated Task",
  "description": "Updated task description",
  "completed": true,
  "date": "2025-05-03"
}
```

To update a task, send a `PUT` request to the task's URL, replacing `{id}` with the task ID. Include the updated task data in the request body as JSON.

```bash

PUT http://127.0.0.1:8000/tasks/1/
Content-Type: application/json

{
  "title": "Updated Task",
  "description": "Updated task description",
  "completed": true,
  "date": "2025-05-03"
}


```


### 5. Delete a Task by ID

**URL:** `/tasks/{id}/`
**Method:** `DELETE`
**Description:** Deletes a specific task by its ID.
**Usage:**

To delete a task, send a `DELETE` request to the task's URL, replacing `{id}` with the ID of the task you want to delete.

**Example using `curl`:**

```bash
curl -X DELETE [http://127.0.0.1:8000/tasks/1/](http://127.0.0.1:8000/tasks/1/)

```


You can filter the list of tasks based on specific fields such as completed status or date. The following query parameters are supported:

### 6. Filter by Completed Status

**URL:** `/tasks/?completed=<value>`
**Method:** `GET`
**Description:** Filters tasks based on their completion status.
* `completed=true`: Fetch only tasks marked as completed.
* `completed=false`: Fetch only tasks that are not completed.
**Example:**

To retrieve all completed tasks:

```bash
curl [http://127.0.0.1:8000/tasks/?completed=true](http://127.0.0.1:8000/tasks/?completed=true)
```

### 7. Filter by Date

**URL:** `/tasks/?date=YYYY-MM-DD`
**Method:** `GET`
**Description:** Filters tasks based on their creation date.

Use the date format `YYYY-MM-DD` to filter tasks created on a specific date.

**Example:**

To retrieve all tasks created on May 3rd, 2025:

```bash
curl [http://127.0.0.1:8000/tasks/?date=2025-05-03](http://127.0.0.1:8000/tasks/?date=2025-05-03)
```


---



## 🐳 Docker Setup (Optional)

You can use Docker to build and run the project in a containerized environment.

**Build and Run the Project with Docker:**

```bash
docker-compose up --build
```

This command, `docker-compose up --build`, is quite handy. It first checks if the Docker image for your project has been built. If not, it goes ahead and builds it based on the instructions in your `Dockerfile`. After the image is ready, it spins up the containers defined in your `docker-compose.yml` file, effectively launching your application and any dependent services you might have configured (like databases or other utilities).

Then, when you want to shut things down cleanly, the `docker-compose down` command comes into play. It gracefully stops all the running containers that were started by the `up` command and then removes them. This helps to free up resources on your system.


---


## ✅ Running Tests

You can run the project's tests using the Django management command:

```bash
python manage.py test
```

This command will discover and execute all the tests defined in your project's test files.



---

###  📌 Notes

* This project utilizes **Django REST Framework** for building the API.
* All API responses are formatted in **JSON**.
* It's recommended to have your **virtual environment activated** when working on the project locally to manage dependencies effectively.

#### 🔧 Commands
- `python manage.py migrate`: Applies database migrations to set up the schema for the project.
- `python manage.py runserver`: Starts the Django development server to make the API accessible locally.
- `python manage.py test`: Runs the unit tests for the application, ensuring everything works as expected.

#### 🛠 Viewsets
- The **TaskViewSet** is responsible for handling requests related to tasks, including listing, creating, updating, and deleting tasks.
- It provides CRUD functionality through the `list`, `create`, `retrieve`, `update`, and `destroy` actions.
- Viewsets are automatically mapped to URLs via the router configuration.

#### 🧳 Serializers
- The **TaskSerializer** is used to validate and serialize data for task objects, ensuring data integrity and proper format.
- It converts task model instances into JSON data for API responses and validates incoming data for new tasks or updates.
- Serializers handle the transformation of the data from Python objects to JSON and vice versa.

#### 🔗 URL Names
- `/tasks/`: Mapped to the **TaskViewSet** for listing tasks and creating a new task.
- `/tasks/{id}/`: Mapped to the **TaskViewSet** for retrieving, updating, or deleting a specific task by its ID.
- The URLs follow Django's standard routing convention and are connected with viewsets through the router.


## Author and Developer
* Devesh 

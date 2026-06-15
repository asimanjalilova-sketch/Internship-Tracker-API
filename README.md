# Internship Tracker API

A RESTful backend API built with FastAPI for managing internship applications. The project allows users to register, authenticate using JWT tokens, and securely track their internship application process.

## Features

### Authentication

* User registration
* Secure password hashing with bcrypt
* User login
* JWT-based authentication
* Protected API endpoints

### Application Management

* Create internship applications
* View all applications
* View a specific application
* Update application details
* Delete applications
* Filter applications by status

### Database

* PostgreSQL database integration
* SQLAlchemy ORM
* User-to-application relationship

## Technologies Used

* Python 3
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Passlib (bcrypt)
* Python-JOSE (JWT)
* Uvicorn

## API Endpoints

### Authentication

| Method | Endpoint  | Description                             |
| ------ | --------- | --------------------------------------- |
| POST   | /register | Register a new user                     |
| POST   | /login    | Authenticate user and receive JWT token |

### Applications

| Method | Endpoint           | Description              |
| ------ | ------------------ | ------------------------ |
| GET    | /applications      | Get all applications     |
| POST   | /applications      | Create a new application |
| GET    | /applications/{id} | Get application by ID    |
| PUT    | /applications/{id} | Update application       |
| DELETE | /applications/{id} | Delete application       |

## Application Status Examples

Applications can be tracked using statuses such as:

* Applied
* Interview
* Assessment
* Offer
* Rejected

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/internship-tracker-api.git
cd internship-tracker-api
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE internship_tracker;
```

Update the database connection string in `database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/internship_tracker"
```

### Run the application

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## Example Workflow

1. Register a new user.
2. Login to receive a JWT token.
3. Authorize using the token in Swagger UI.
4. Create internship applications.
5. Update application statuses as you progress through the hiring process.
6. Filter applications by status.

## Future Improvements

* Refresh tokens
* Pagination
* Search functionality
* Email notifications
* Docker support
* Frontend dashboard
* Deployment to cloud platforms

## Author

Computer Science student project built to practice backend development with FastAPI, PostgreSQL, authentication, and REST API design.

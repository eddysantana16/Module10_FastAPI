# FastAPI Secure User Application

This project is a FastAPI application that implements a secure user model using SQLAlchemy and Pydantic. It includes user registration, password hashing, schema validation, testing, and is containerized using Docker with a full CI/CD pipeline via GitHub Actions and Docker Hub.

## Features

- Secure user model with password hashing using `passlib`
- Pydantic schema validation for `UserCreate` and `UserRead`
- Unit and integration testing using `pytest` and a PostgreSQL container
- Continuous Integration with GitHub Actions
- Docker containerization and deployment to Docker Hub

## Project Structure
- module10_is601/
    - ├── app/
    - │ ├── init.py
    - │ ├── main.py
    - │ ├── models.py
    - │ ├── schemas.py
    - │ ├── security.py
    - │ ├── database.py
    - │ └── routers/
    - │ └── users.py
    - ├── tests/
    - │ ├── init.py
    - │ ├── test_security.py
    - │ └── test_users.py
    - ├── requirements.txt
    - ├── Dockerfile
    - ├── pytest.ini
    - └── .github/
    - └── workflows/
    - └── ci.yml

## Running the App Locally

- Make sure you have Python 3.11 and PostgreSQL installed locally, or use Docker to simulate the DB.

## Run with Docker

- docker pull eddysantana/fastapi-userapp:latest
- docker run -d -p 8000:8000 eddysantana/fastapi-userapp:latest
- Open your web browser: http://localhost:8000/docs

## CI/CD Workflow
- GitHub Actions is configured to:
- Spin up a PostgreSQL container
- Install dependencies
- Run unit + integration tests
- If all tests pass, build and push the Docker image to Docker Hub
- File: .github/workflows/ci.yml

## Docker Hub Repository
- Docker Image URL: https://hub.docker.com/r/eddysantana/fastapi-userapp

## Author
- Eddy Santana
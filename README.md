# Aula FastAPI

A simple project to demonstrate building APIs with FastAPI.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project is an example of how to create a fast and efficient API using [FastAPI](https://fastapi.tiangolo.com/). It serves as a learning tool and template for building more complex applications.

## Features
- **Fast** and modern Python web framework.
- Easy to set up API endpoints.
- Automatic interactive API documentation with Swagger UI and ReDoc.
- Asynchronous request handling.

## Installation
1. **Clone the repository:**
    ```
    git clone https://your-repo-url.git
    cd your-repo-directory
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

## Usage
1. **Run the application:**
    ```
    uvicorn main:app --reload
    ```

2. **Access the API documentation:**
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
# FastAPI with Google Firebase Database

This project demonstrates how to create a backend API using FastAPI and Google Firebase as the database. It includes features for user sign-up, login with JWT token generation, and fuzzy matching of job names.

## Features

- User sign-up
- User login with JWT token generation
- JWT token validation
- Fuzzy matching of job names

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Firebase](https://firebase.google.com/)
- [Python-Jose](https://github.com/mpdavis/python-jose) for JWT handling
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) for fuzzy matching

## Getting Started

### Prerequisites

- Python 3.11+
- Firebase account with Firestore setup

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NilayDev/ramped-backend.git
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    ## On Linux use source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firebase:

    - Go to [Firebase Console](https://console.firebase.google.com/).
    - Create a new project.
    - Enable Firestore in the database section.
    - Download the `serviceAccountKey.json` file and place it in the project root.

5. Create a `.env` file in the project root and add the following:

    ```env
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    FIREBASE_CREDENTIALS=path/to/serviceAccountKey.json
    ```

6. For creating example job deatils table in database run job details import data file
        
        ```bash
        python job_details_import_data.py
        ```

### Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

- **Sign Up**
    - **URL:** `/signup`
    - **Method:** `POST`
    - **Body:**
      ```json
      {
          "username": "your_username",
          "password": "your_password"
      }
      ```
    - **Response:**
      ```json
      {
          "message": "User created successfully"
      }
      ```

- **Login**
    - **URL:** `/login`
    - **Method:** `POST`
    - **Body:**
      ```json
      {
          "username": "your_username",
          "password": "your_password"
      }
      ```
    - **Response:**
      ```json
      {
          "access_token": "your_jwt_token",
          "token_type": "bearer"
      }
      ```

- **Fuzzy Match Job Names**
    - **URL:** `/fuzzy-match`
    - **Method:** `POST`
    - **Headers:**
      ```http
      Authorization: Bearer your_jwt_token
      ```
    - **Body:**
      ```json
      {
          "job_name": "example_job_name"
      }
      ```
    - **Response:**
      ```json
      [
          {
              "job_id": "1",
              "job_name": "example_job_name"
          },
          ...
      ]
      ```


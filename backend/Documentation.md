# FastAPI Simple Auth Project

## Overview
This project is a simple backend authentication system using FastAPI, SQLModel, and MySQL. It provides basic user registration, login, and profile retrieval endpoints with JWT-based authentication.

## Features
- User registration (`/register`)
- User login with JWT token generation (`/login`)
- Profile endpoint to get user info (`/profile`)
- Uses MySQL as the database
- Passwords are stored as plain text (for demo only; use hashing in production)

## Tech Stack
- FastAPI
- SQLModel
- MySQL
- PyJWT
- Uvicorn (for running the server)

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Ensure MySQL is running and accessible with user `root` and password `Nayan@123`.
3. The database and table are created automatically on first run.
4. Start the server:
   ```
   uvicorn main:app --reload
   ```

## Endpoints
- `POST /register` — Register a new user
- `POST /login` — Login and receive JWT token
- `POST /profile` — Get user info (requires token)

## Security Note
- For demo purposes, passwords are not hashed. In production, always hash passwords before storing.
- Use a strong, secret key for JWT.

## Author
- Your Name

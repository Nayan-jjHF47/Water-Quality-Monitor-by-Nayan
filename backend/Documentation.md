
# WaterWatch: Real-Time Water Quality Monitoring Platform

## Milestone 1: Weeks 1–2 – Setup & Auth

### Project Statement
Enables real-time water quality monitoring for communities and authorities, providing open data dashboards, user reports, and alerts for contamination.

### What Was Done (by Nayan Pawar)
- FastAPI backend initialized
- Database schema created (using SQLModel/MySQL for demo, PostgreSQL for production)
- User registration and login endpoints implemented
- JWT authentication integrated
- requirements.txt and documentation provided

### Database Schema (for Milestone 1)
- **Users:**
    - id (INT, PK): Unique user ID
    - name (VARCHAR): User's full name
    - email (VARCHAR, UNIQUE): User's email address (unique)
    - password (VARCHAR): User's password
    - role (ENUM: 'citizen','ngo','authority','admin'): User role (default: 'citizen')
    - location (VARCHAR): User's location (optional)
    - created_at (TIMESTAMP): Account creation date/time

### Tech Stack (for Milestone 1)
- Backend: FastAPI
- Database: PostgreSQL (MySQL used for demo)
- Auth: JWT

### Setup
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

### Endpoints
- `POST /register` — Register a new user
- `POST /login` — Login and receive JWT token
- `POST /profile` — Get user info (requires token)

### Security Note
- For demo purposes, passwords are not hashed. In production, always hash passwords before storing.
- Use a strong, secret key for JWT.

---

**Milestone 1 (Weeks 1 & 2) completed by Nayan Pawar**

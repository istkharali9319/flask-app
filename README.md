# Flask Project API

This repository contains a Flask backend with a simple MVC-style structure for profile data, authentication, roles, users, AI conversation flows, and brochure generation.

## Features

- Flask application factory setup
- SQLAlchemy models and Flask-Migrate migrations
- JWT-ready auth flow
- User, role, and profile APIs
- Conversation and message endpoints
- Sales brochure HTML page and brochure generation endpoint

## Project Structure

```text
app/
  controllers/
  models/
  repositories/
  routes/
  services/
  utils/
migrations/
run.py
requirements.txt
```

## Main Endpoints

- `GET /`
- `GET /health`
- `GET /api/profile/`
- `POST /api/auth/login`
- `GET /api/users/`
- `POST /api/users/create`
- `PUT /api/users/update/<id>`
- `DELETE /api/users/delete/<id>`
- `GET /api/roles/`
- `POST /api/roles/create`
- `PUT /api/roles/update/<id>`
- `DELETE /api/roles/delete/<id>`
- `GET /api/conversations`
- `POST /api/conversations/chat`
- `POST /api/conversations/stream`
- `GET /api/conversations/<conversation_id>/messages`
- `GET /api/sales-company-brochure`
- `POST /api/brochure/generate`

## Requirements

- Python 3.10+
- PostgreSQL

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Create a `.env` file with your database and app settings, then start the server:

```bash
python run.py
```

The app runs on `http://127.0.0.1:5000` by default.

## Notes

- Database schema changes are managed with Flask-Migrate in `migrations/`.
- CORS is configured for local frontend ports `5173` and `5174`.
- The brochure endpoints use the `sales-company-brochure` directory and the AI service layer.

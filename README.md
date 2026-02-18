# FastAPI + SQLAlchemy User API

## Folder Structure

```
app/
  core/
    config.py
  db/
    database.py
    session.py
  models/
    user.py
  repository/
    user_repository.py
  routes/
    users.py
  schemas/
    user.py
  init_db.py
  main.py
```

## Setup

1. Create and activate virtual env.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create `.env` from `.env.example` and set Vercel Postgres URI:
   ```env
   DATABASE_URL=postgresql://username:password@host:5432/database
   ```
   or
   ```env
   POSTGRES_URL=postgresql://username:password@host:5432/database
   ```
4. Run app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

- `GET /` hello world
- `POST /users/` create user
- `GET /users/` get all users
- `GET /users/{user_id}` get user by id

## Deploy on Vercel (Bonus)

1. Push repository to GitHub.
2. Import project in Vercel.
3. Add env variable `DATABASE_URL` or `POSTGRES_URL` from Vercel Postgres.
4. Deploy.

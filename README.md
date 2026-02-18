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

## Local Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create `.env` from `.env.example`.
3. Run:
   ```bash
   uvicorn app.main:app --reload
   ```

## API

- `GET /`
- `GET /health`
- `POST /users/`
- `GET /users/`
- `GET /users/{user_id}`

## Deploy Options

### Option 1: Render / Railway

- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Env var: set `DATABASE_URL` (or `POSTGRES_URL`)

### Option 2: Docker (Any VPS/Cloud)

```bash
docker build -t fastapi-user-service .
docker run -p 8000:8000 --env-file .env fastapi-user-service
```

### Option 3: Vercel

1. Import repo in Vercel.
2. Keep `vercel.json` as is.
3. Set `DATABASE_URL` or `POSTGRES_URL` in Vercel Environment Variables.
4. Deploy.

## Notes

- Both `postgres://` and `postgresql://` are accepted by config.
- App auto-creates tables on startup.

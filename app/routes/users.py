from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repository import user_repository
from app.schemas.user import UserCreate, UserOut

router = APIRouter()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserOut:
    existing = user_repository.get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    return user_repository.create_user(db, payload)


@router.get("/", response_model=list[UserOut])
def get_all_users(db: Session = Depends(get_db)) -> list[UserOut]:
    return user_repository.get_all_users(db)


@router.get("/{user_id}", response_model=UserOut)
def get_user_by_user_id(user_id: int, db: Session = Depends(get_db)) -> UserOut:
    user = user_repository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
